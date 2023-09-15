var once = function(fn) {
    let cnt = 0
    return function(...args){
        if(cnt === 0) {
            cnt++;
            return fn(...args)
        } else {
            return undefined;
        }
    }
};