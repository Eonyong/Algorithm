function solution(elements) {
    let answer = new Set();
    let n = elements.length;
    let ls = Array.from({length: n}).fill(0);
    
    for(let i = 0;i <n;i++) {
        for(let idx = 0; idx < n; idx++) {
            ls[idx] += elements[(idx + i) % n];
            answer.add(ls[idx]);
        };
    };
    
    return answer.size;
}