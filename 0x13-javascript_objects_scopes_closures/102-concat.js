#!/usr/bin/node
// 102-concat.js -  a script that concats 2 files.
const file = require('fs');
const fileArray = process.argv.slice(2);
const firstArg = file.readFileSync(fileArray[0], 'utf-8');
const secondArg = file.readFileSync(fileArray[1], 'utf-8');
file.writeFileSync(fileArray[2], firstArg + secondArg);
