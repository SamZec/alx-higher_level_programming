#!/usr/bin/node
// 100-map.js - a script that imports an array and computes a new array.
const array = require('./100-data').list;
const newArray = array.map((x, index) => x * index);
console.log(array);
console.log(newArray);
