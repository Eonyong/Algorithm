function solution(ingredient) {
    var answer = 0;
    let tmp = []
    for (let i = 0; i < ingredient.length; i++) {
        tmp.push(ingredient[i])
        let l = tmp.length;
        if (l > 3) {
            if ((tmp[l - 4] == 1) && (tmp[l - 3] == 2) && (tmp[l - 2] == 3) && (tmp[l - 1] == 1)) {
                for (let j = 0; j < 4; j++) {
                    tmp.pop()
                }
                answer++
            }
        }
    }
    return answer;
}