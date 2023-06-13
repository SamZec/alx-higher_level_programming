#!/usr/bin/node
// 102-add_me_maybe.js - script for function that increments and calls a function.

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
