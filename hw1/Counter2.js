var createCounter = function(init) {
    a = init;
    function increment() {
        return ++init;
    }
    function decrement() {
        return --init;
    }
    function reset() {
        init = a;
        return init;
    }
    return{increment, decrement, reset}
};