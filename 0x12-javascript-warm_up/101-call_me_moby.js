#!/usr/bin/node
// 101-call_me_moby.js - script for a function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
