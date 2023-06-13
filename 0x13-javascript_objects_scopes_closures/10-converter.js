#!/usr/bin/node
// 10-converter.js - a script with a function that converts a number from base 10
// to another base passed as argument
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
