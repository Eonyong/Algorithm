function solution(n) {
    var answer = 0;
    let m = 1;
    while (m < n) {
        m += 1;
        let cnt = 0;
        for (let i = 1;i < m;i++) {
            if (m % i == 0) cnt += 1;
        }
        if (cnt > 1) answer += 1;
    }
    return answer;
}