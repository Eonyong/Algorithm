function solution(n) {
    let i = 1;
    while (true) {
        if (n % i == 1) {
            return i;
        } else {
            i += 1;
        };
    };
}