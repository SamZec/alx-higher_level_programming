#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const url = process.argv[2];
const request = require('request');

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const tasks = {};
    for (let i = 0; data[i] !== undefined; i++) {
      if (data[i].completed) {
        if (data[i].userId in tasks) {
          tasks[data[i].userId] += 1;
        } else {
          tasks[data[i].userId] = 1;
        }
      }
    }
    console.log(tasks);
  }
});
