#!/usr/bin/node
// a script that prints the number of movies where the
// character “Wedge Antilles” is present.
const url = process.argv[2];
const chrUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const request = require('request');
let count = 0;
request.get(url, function (err, res, body) {
  if (!err) {
    const films = JSON.parse(body);
    for (let i = 0; films.results[i] !== undefined; i++) {
      if (films.results[i].characters.includes(chrUrl)) {
        count++;
      }
    }
  }
  console.log(count);
});
