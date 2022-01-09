const things = require('./module.js');

let args = process.argv.slice(-2)

let op = new things.Operation(args[0], args[1]);

// node index "43" 3
console.log(op.sum())

// Call: node .\index.js 1 "989"