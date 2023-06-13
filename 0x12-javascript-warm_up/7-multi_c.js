#!/usr/bin/node
// 7-multi_c.js - a script that prints x times “C is fun”
// Where x is the first argument of the script

const arg = process.argv.slice(2);
const isNum = isNaN(arg[0]);
if (!isNum) for (let i = 0; i < arg[0]; i++) console.log('C is fun');
else console.log('Missing number of occurrences');
