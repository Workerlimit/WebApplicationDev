var cancellable = function(fn, args, t) {
    const timeout = setTimeout(() => { fn(...args) }, t)
    return () => { clearTimeout(timeout) }
};