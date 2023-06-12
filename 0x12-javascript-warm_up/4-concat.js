#!/usr/bin/node
// 4-concat.js - a script that prints two arguments passed
// to it, in  sentence with “ is ” between

const arg = process.argv.slice(2);
console.log(arg[0] + ' is ' + arg[1]);
