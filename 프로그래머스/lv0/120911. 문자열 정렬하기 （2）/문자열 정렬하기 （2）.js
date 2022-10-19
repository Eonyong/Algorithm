function solution(my_string) {
    let answer = [];
    my_string = my_string.toLowerCase();
    for (let i = 0;i < my_string.length;i++) answer.push(my_string[i]);
    return answer.sort().join('');
}