function solution(x) {
    let n = x;
    let tmp = 0;
    while(n) {
        tmp += n % 10;
        n = parseInt(n / 10);
    };
    if (x % tmp == 0) {
        return true;
    } else {
        return false;
    }
}