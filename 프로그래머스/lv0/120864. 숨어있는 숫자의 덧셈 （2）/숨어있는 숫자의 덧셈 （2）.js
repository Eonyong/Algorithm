function solution(my_string) {
    var answer = 0;
    let nums = my_string.match(/[0-9]+/g)
//     nums의 값을 String => Number 탕비 변경 뒤
//     초기값 answer를 a로 저장하여 v를 계속 더하고 이를 리턴
    return nums ? nums.map(num => Number(num)).reduce((a, v) => a + v, answer) : 0
}