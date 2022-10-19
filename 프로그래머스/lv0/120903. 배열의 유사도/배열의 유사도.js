function solution(s1, s2) {
    var answer = 0;
    s1.forEach(e => {
        s2.forEach(m => {
            if (e == m) {
                answer += 1;
            }
        })
    })
    return answer;
}