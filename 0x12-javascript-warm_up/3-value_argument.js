#!/usr/bin/node
// 3-value_argument.js - a script that prints the first argument passed to it
// If no arguments are passed to the script, print “No argument”

const arg = process.argv.slice(2);
if (arg[0] !== undefined) console.log(arg[0]);
else console.log('No argument');
