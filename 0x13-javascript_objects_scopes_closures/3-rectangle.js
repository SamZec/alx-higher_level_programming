#!/usr/bin/node
// 3-rectangle.js - script with a class Rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0 && !isNaN(w)) && (h > 0 && !isNaN(h))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shape = '';
    for (let wdth = 1; wdth <= this.width; wdth++) {
      shape += 'X';
    }
    for (let hght = 1; hght <= this.height; hght++) {
      console.log(shape);
    }
  }
};
