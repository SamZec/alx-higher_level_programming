#!/usr/bin/node
// 11-second_biggest.js - a script that searches the second biggest integer in the list of arguments.

function secondMax (numArray) {
  let max = 0;
  let result = 0;
  for (const value of numArray) {
    const newResult = Number(value);
    if (newResult > max) {
      [result, max] = [max, newResult];
    } else if (newResult < max && newResult > result) {
      result = newResult;
    }
  }
  return result;
}
console.log(secondMax(process.argv));
