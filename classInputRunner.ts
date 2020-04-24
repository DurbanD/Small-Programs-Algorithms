interface BuildableClass {
    new(...args:any),
}

const runInputs = function(cls:BuildableClass, names:Array<string>, args:Array<Array<any>>) {
    let inputHistory = [];
    if (names.length !== args.length) {
        return 'Unable to run due to unequal array length';
    }
    else {
        let calledClass = new cls(args[0][0]);
        inputHistory.push('init');
        for (let i = 1; i < args.length; i++) {
            let method = eval(`calledClass.${names[i]}`);
            inputHistory.push(`${method.apply(calledClass,args[i])}`);
        }
    }
    return `Inputs Completed Successfully. [${inputHistory}]`
}

// Takes a constructable class, an array of method names, and a second array containing arguments in an array
// Argument and Method Name variables must be equal in length
// The First item of each array will be used to call the class constructor.

// Example =>
// class Mather {
//     constructor() {
//     }
//
//    add(x,y) {
//        return x + y;
//    }
// }
//
// runInputs(Mather,["Mather","add"],[[''],[1,1]]); => [init,2]
