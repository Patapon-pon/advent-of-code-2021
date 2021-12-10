function simulate_births(initial: number[], days: number): number {
    const birth_calender: number[] = [];
    const delta = 7;
    const deltaB = 9;

    for (let day = 0; day < days + deltaB; day++) {
        birth_calender[day] = 0;
    }

    initial.forEach(fish => {
        birth_calender[fish] += 1
    });


    let population = initial.length;
    for (let day = 0; day < days; day++) {
        let births = birth_calender[day];
        if (births !== 0) {
            population += births;
            birth_calender[day + delta] += births;
            birth_calender[day + deltaB] += births;
        }
    }

    return population;
}

const input = [5, 1, 5, 3, 2, 2, 3, 1, 1, 4, 2, 4, 1, 2, 1, 4, 1, 1, 5, 3, 5, 1, 5, 3, 1, 2, 4, 4, 1, 1, 3, 1, 1, 3, 1, 1, 5, 1, 5, 4, 5, 4, 5, 1, 3, 2, 4, 3, 5, 3, 5, 4, 3, 1, 4, 3, 1, 1, 1, 4, 5, 1, 1, 1, 2, 1, 2, 1, 1, 4, 1, 4, 1, 1, 3, 3, 2, 2, 4, 2, 1, 1, 5, 3, 1, 3, 1, 1, 4, 3, 3, 3, 1, 5, 2, 3, 1, 3, 1, 5, 2, 2, 1, 2, 1, 1, 1, 3, 4, 1, 1, 1, 5, 4, 1, 1, 1, 4, 4, 2, 1, 5, 4, 3, 1, 2, 5, 1, 1, 1, 1, 2, 1, 5, 5, 1, 1, 1, 1, 3, 1, 4, 1, 3, 1, 5, 1, 1, 1, 5, 5, 1, 4, 5, 4, 5, 4, 3, 3, 1, 3, 1, 1, 5, 5, 5, 5, 1, 2, 5, 4, 1, 1, 1, 2, 2, 1, 3, 1, 1, 2, 4, 2, 2, 2, 1, 1, 2, 2, 1, 5, 2, 1, 1, 2, 1, 3, 1, 3, 2, 2, 4, 3, 1, 2, 4, 5, 2, 1, 4, 5, 4, 2, 1, 1, 1, 5, 4, 1, 1, 4, 1, 4, 3, 1, 2, 5, 2, 4, 1, 1, 5, 1, 5, 4, 1, 1, 4, 1, 1, 5, 5, 1, 5, 4, 2, 5, 2, 5, 4, 1, 1, 4, 1, 2, 4, 1, 2, 2, 2, 1, 1, 1, 5, 5, 1, 2, 5, 1, 3, 4, 1, 1, 1, 1, 5, 3, 4, 1, 1, 2, 1, 1, 3, 5, 5, 2, 3, 5, 1, 1, 1, 5, 4, 3, 4, 2, 2, 1, 3]


console.log(simulate_births(input, 80))
console.log(simulate_births(input, 256))
