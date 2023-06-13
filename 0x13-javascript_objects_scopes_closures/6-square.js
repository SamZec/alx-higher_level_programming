#!/usr/bin/node
// 6-square.js - a script for class Square that defines a square and inherits from Square of 5-square.js
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    let chr;
    let shape = '';
    if (c !== undefined) {
      chr = 'C';
    } else {
      chr = 'X';
    }
    for (let wdth = 1; wdth <= this.size; wdth++) {
      shape += chr;
    }
    for (let hght = 1; hght <= this.size; hght++) {
      console.log(shape);
    }
  }
};
