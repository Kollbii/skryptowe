import { Operation } from './module.mjs'

let num1 = parseInt(process.argv[2]);
let num2 = parseInt(process.argv[3]);

let op1 = new Operation('1', 337);
let op2 = new Operation(num1, num2);
console.log(op1.sum());
console.log(op2.sum());