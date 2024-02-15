#!/usr/bin/node

const request = require('request');

const API = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(API, (err, response, body) => {
  if (!err) {
    const charAPI = JSON.parse(body).characters;
    print(charAPI, 0);
  }
});

function print (charAPI, i) {
  request(charAPI[i], (err, response, body) => {
    if (!err) {
      const char = JSON.parse(body);
      console.log(char.name);
      if (i + 1 < charAPI.length) {
        print(charAPI, i + 1);
      }
    }
  });
}
