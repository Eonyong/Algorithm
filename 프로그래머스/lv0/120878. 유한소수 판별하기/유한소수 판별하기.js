function val(num) {
    while (true) {
        if (!(num % 10)) num /= 10
        else if (!(num % 5)) num /= 5
        else if (!(num % 2)) num /= 2
        else return num
    }
}

function solution(a, b) {
    if (val(a) % val(b)) return 2
    else return 1
}