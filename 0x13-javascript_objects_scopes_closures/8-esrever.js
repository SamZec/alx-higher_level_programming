#!/usr/bin/node
// 8-esrever.js -  a script with a function that returns the reversed version of a list
exports.esrever = function (list) {
  const revList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
