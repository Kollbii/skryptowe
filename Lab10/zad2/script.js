const { isDir } = require('./module_zad2');

let args = process.argv.slice(-1);
console.log(isDir(args[0]))
