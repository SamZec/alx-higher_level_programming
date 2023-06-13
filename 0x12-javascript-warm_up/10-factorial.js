#!/usr/bin/node
// 10-factorial.js - a script that computes and prints a factorial

function factorial (a) {
  if (isNaN(a))
    return 1
  else if (a === 0)
    return 1
  else
    return (a * factorial(a - 1))
}
const arg = process.argv.slice(2);
const num = parseInt(arg[0]);
const fact = factorial(num);
console.log(fact);
