with open("input.txt") as f:
    data = [line.strip("\n") for line in f.readlines()]


def part1():
    unique_segment_sizes = [2, 3, 4, 7]
    answer = 0
    for line in data:
        output = line.split(" | ")[1]
        for segment in output.split():
            if len(segment) in unique_segment_sizes:
                answer += 1
    return answer


def part2():
    def count_occurrences(str1, str2) -> int:
        occurrences = 0
        for letter in str1:
            if letter in str2:
                occurrences += 1
        return occurrences

    result_sum = 0
    for line in data:
        signals = list(sorted(["".join(sorted(signal)) for signal in line.split(" | ")[0].split(" ")],
                              key=lambda x: len(x)))
        simple_numbers = [1, 7, 4, 8]
        simple_segments = signals[:3] + signals[-1:]
        configuration = dict(zip(simple_numbers, simple_segments))
        for five_segment_number in signals[3:6]:
            if count_occurrences(five_segment_number, configuration[7]) == 3:
                configuration[3] = five_segment_number
            elif count_occurrences(five_segment_number, configuration[4]) == 3:
                configuration[5] = five_segment_number
            else:
                configuration[2] = five_segment_number
        for six_segment_number in signals[6:9]:
            if count_occurrences(six_segment_number, configuration[1]) == 1:
                configuration[6] = six_segment_number
            elif count_occurrences(six_segment_number, configuration[4]) == 4:
                configuration[9] = six_segment_number
            else:
                configuration[0] = six_segment_number

        flipped_configurations = dict((segment, number) for number, segment in configuration.items())
        output_numbers = ["".join(sorted(out)) for out in line.split(" | ")[1].split(" ")]
        result_sum += int("".join([str(flipped_configurations[number]) for number in output_numbers]))

    return result_sum


print(part1())
print(part2())
