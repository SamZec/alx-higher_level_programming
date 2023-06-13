#!/usr/bin/node
// 9-add.js - a script that prints the addition of 2 integers

const arg = process.argv.slice(2);
function add (a, b) {
  const num1 = parseInt(arg[0], 10);
  const num2 = parseInt(arg[1], 10);
  return (num1 + num2);
}
const result = add(arg[0], arg[1]);
console.log(result);
