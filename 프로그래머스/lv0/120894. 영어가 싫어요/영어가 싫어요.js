function solution(numbers) {
    var answer = 0;
    let num = [["zero", "0"], ["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]]
    for (const value of num) {
        let [v, k] = value
        numbers = numbers.replaceAll(v, k)
    }
    return parseInt(numbers);
}