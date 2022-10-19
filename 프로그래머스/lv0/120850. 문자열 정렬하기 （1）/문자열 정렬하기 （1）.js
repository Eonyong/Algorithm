function solution(my_string) {
    let answer = [];
    for (let i = 0;i < my_string.length;i++) {
        if (my_string[i] == '0') answer.push(0);
        else if (Number(my_string[i])) answer.push(Number(my_string[i]));
    }
    
    return answer.sort();
}