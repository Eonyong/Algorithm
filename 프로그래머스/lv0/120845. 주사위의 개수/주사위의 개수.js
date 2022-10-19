function solution(box, n) {
    let answer = 1;
    box = box.map(e => parseInt(e / n));
    box.forEach(e => answer *= e);
    return answer;
}