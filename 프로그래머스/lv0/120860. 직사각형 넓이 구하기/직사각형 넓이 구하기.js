function solution(dots) {
    var answer = 0;
    let [x_min, x_max, y_min, y_max] = [300, -300, 300, -300]
    for (let dot of dots) {
        let [x, y] = dot
        x_min = x_min > x ? x : x_min 
        x_max = x_max > x ? x_max : x
        y_min = y_min > y ? y : y_min
        y_max = y_max > y ? y_max: y
    }
    
    return (x_max - x_min) * (y_max - y_min)
}