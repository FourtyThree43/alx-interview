#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charData = movieData.characters;

    charData.forEach((charUrl) => {
      request.get(charUrl, (err, response, body) => {
        if (err) {
          console.error(err);
        } else if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.log(`Error code: ${response.statusCode}`);
        }
      });
    });
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});
