function solution(hp) {
    let answer = 0;
    for (let king = parseInt(hp / 5);king >= 0;king--) {
        if ((hp - king * 5) % 3 == 0) {
            return king + parseInt((hp - king * 5) / 3);
        }
        else {
            return king + parseInt((hp - king * 5) / 3) + (hp - king * 5) % 3;
        }
    }
    return answer;
}