var expect = function(val) {
    return {
        toBe:(a) => {
            if(val === a) {
                return true
            } else {
                throw new Error("Not Equal")
            }
        },
        notToBe:(a) => {
            if(val !== a) {
                return true
            } else {
                throw new Error("Equal")
            }
        }
    }
};
