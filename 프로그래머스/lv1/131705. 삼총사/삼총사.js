function solution(number) {
    let answer = 0;
    let n = number.length;
    
    for (let i = 0; i < n - 2; i++) {
        for (let j = i + 1; j < n - 1; j++) {
            for (let k = j + 1; k < n; k++) {
                let v = number[i] + number[j] + number[k];
                if (v === 0) {
                    answer += 1;
                };
            };
        };
    };
    
    return answer;
}