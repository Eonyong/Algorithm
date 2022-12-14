function solution(sides) {
    var answer = 0;
    let [minVal, maxVal] = sides[0] > sides[1] ? [sides[1], sides[0]] : [sides[0], sides[1]]
    let sumVal = sides.reduce((a, v) => a + v, 0)
    
    for (let i = 1; i <= maxVal; i ++) {
        answer += maxVal < minVal + i ? 1 : 0
    }
    for (let i = maxVal + 1; i <= sumVal; i++) {
        answer += sumVal > i ? 1 : 0
    }
    
    return answer;
}