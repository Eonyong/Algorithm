function solution(num, k) {
    num = num.toString();
    for (let i = 0;i < num.length;i++) {
        if (parseInt(num[i]) == k) return i + 1;
    }
    return -1;
}