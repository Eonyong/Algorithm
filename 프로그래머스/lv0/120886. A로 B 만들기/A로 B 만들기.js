function solution(before, after) {
    var answer = 0;
    before = Array.from(before).sort();
    after = Array.from(after).sort();
    for (let i = 0; i < after.length;i++) {
        if(before[i] != after[i]) return 0;
    }
    return 1;
}