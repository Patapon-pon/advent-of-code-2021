package main;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Direction {
    private final String direction;
    private final int steps;

    public Direction(String direction, int steps) {
        this.direction = direction;
        this.steps = steps;
    }

    public int getSteps() {
        return steps;
    }

    public String getDirection() {
        return direction;
    }
}

class InstructionParser {

    public static Direction parse(String instruction) {
        String[] directionAndSteps = instruction.split(" ");
        String movement = directionAndSteps[0];
        int steps = Integer.parseInt(directionAndSteps[1]);

        switch (movement) {
            case "forward": {
                return new Direction("horizontal", steps);
            }
            case "up": {
                return new Direction("depth", -steps);
            }
            case "down": {
                return new Direction("depth", steps);
            }
            default: {
                throw new IllegalArgumentException("Unknown movement");
            }
        }
    }
}

public class Submarine {

    private final Map<String, Integer> positionalData = new HashMap<>();

    public Submarine() {
        positionalData.put("horizontal", 0);
        positionalData.put("depth", 0);
        positionalData.put("aim", 0);
    }


    public int dive(List<String> data) {
        for (String instruction: data) {
            Direction order = InstructionParser.parse(instruction);
            updatePosition(order);

        }
        return calculateCross();
    }

    private void updatePosition(Direction order) {
        String key = order.getDirection();
        if (key.equals("depth")) {
            positionalData.put("aim", positionalData.get("aim") + order.getSteps());
        } else {
            positionalData.put(key, positionalData.get(key) + order.getSteps());
            int currentDepth = positionalData.get("depth");
            int newDepth = currentDepth + (order.getSteps() * positionalData.get("aim"));
            positionalData.put("depth", newDepth);
        }
    }

    private int calculateCross() {
        return positionalData.get("horizontal") * positionalData.get("depth");
    }

    public static void main(String[] args) {
        List<String> data = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader("src/main/input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                data.add(line);
            }
        } catch (IOException e) {
            throw new RuntimeException("Couldn't find file input.txt");
        }

        Submarine submarine = new Submarine();
        System.out.println(submarine.dive(data));
    }
}
