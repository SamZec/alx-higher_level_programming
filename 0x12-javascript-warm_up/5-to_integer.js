#!/usr/bin/node
// 5-to_integer.js - a script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer.

const arg = process.argv.slice(2);
const isNum = isNaN(arg[0]);
if (isNum) console.log('Not a number');
else console.log('My number: ' + arg[0]);
