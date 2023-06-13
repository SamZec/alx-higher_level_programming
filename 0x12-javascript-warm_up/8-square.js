#!/usr/bin/node
// 8-square.js - a script that prints a square

const arg = process.argv.slice(2);
const isNotNum = isNaN(arg[0]);
if (isNotNum) console.log('Missing size');
else {
  let line = '';
  for (let i = 1; i <= arg[0]; i++) {
    line += 'X';
  }
  for (let i = 1; i <= arg[0]; i++) {
    console.log(line);
  }
}
