function solution(i, j, k) {
    var answer = 0;
    for (let m = i;m<=j;m++) {
        answer += Array.from(m.toString()).filter(e => e == k).length;
    }
    return answer;
}