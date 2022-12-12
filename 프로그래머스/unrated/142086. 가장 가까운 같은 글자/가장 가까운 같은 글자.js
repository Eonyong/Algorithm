function solution(s) {
    var answer = [];
    for (let i = 0; i < s.length; i++) {
        let tmp = -1;
        for (let j = 0; j < i; j++) {
            if (s[i] == s[j]) tmp = i - j;
        }
        answer.push(tmp)
    }
    return answer;
}