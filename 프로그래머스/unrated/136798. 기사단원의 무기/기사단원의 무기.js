function solution(number, limit, power) {
    var answer = 0;
    for (let i = 1; i <= number; i++) {
        if (i < 3) {
            if (i > limit) answer += power
            else answer += i
        }
        else {
            let val = 0;
            for (let j = 1; j <= (i ** .5); j++) {
                if (i % j == 0) {
                    if ((i / j) == j) {
                        val += 1
                    }
                    else val += 2
                }
            }
            if (val <= limit) answer += val
            else answer += power
        }
    }
    return answer;
}