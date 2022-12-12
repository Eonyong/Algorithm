function solution(babbling) {
    var answer = 0;
    speakers = ["ye", "ma", "woo", "aya"];
    for(let bab of babbling) {
        let indexes =  {"ye": [], "ma": [], "woo": [], "aya": []};
        let idx = 0;
        let rounds = false;
        while (idx < bab.length) {
            let tf = false
            for (let sp of speakers) {
                if (sp === bab.slice(idx, idx + sp.length)) {
                    if ((indexes[sp] !== []) && (indexes[sp].pop() + sp.length == idx)) {
                        tf = false
                        break
                    }
                    indexes[sp].push(idx)
                    idx += sp.length
                    tf = true
                    break
                }
            }
            if (!tf) break
            if (idx == bab.length) {
                rounds = true
                break
            }
        }
        if (rounds) answer++
    }
    return answer;
}