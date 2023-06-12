#!/usr/bin/node
// 2-arguments.js - a script that prints a message depending of the
// number of arguments passed

const arg = process.argv.slice(2);
if (arg.length === 0) console.log('No argument');

else if (arg.length === 1) console.log('Argument found');

else console.log('Arguments found');
