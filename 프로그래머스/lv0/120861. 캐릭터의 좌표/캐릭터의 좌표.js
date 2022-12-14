function solution(keyinput, board) {
    var [ni, nj] = [0, 0];
    let [x, y] = [(board[0] - 1) / 2, (board[1] - 1) / 2]
    for (const key of keyinput) {
        if (key === "left") {
            ni = ni - 1 < -x ? -x : ni - 1
        }
        else if (key === "right") {
            ni = ni + 1 > x ? x : ni + 1
        }
        else if (key === "down") {
            nj = nj - 1 < -y ? -y : nj - 1
        }
        else if (key === "up") {
            nj = nj + 1 > y ? y : nj + 1
        }
    }
    return [ni, nj];
}