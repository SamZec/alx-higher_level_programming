#!/usr/bin/node
// 6-square.js - a script for class Square that defines a square and inherits from Square of 5-square.js
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print()
    } else {
      let shape = ''
      for (let wdth = 1; wdth <= this.width; wdth++) {
        shape += 'C';
      }
      for (let hght = 1; hght <= this.height; hght++) {
        console.log(shape);
      }
    }
  }
};
