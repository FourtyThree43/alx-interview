#!/usr/bin/node
const request = require('request');

function fetch(url) {
	return new Promise((resolve, reject) => {
		request.get(url, (err, response, body) => {
			if (err) {
				reject(err);
			} else if (response.statusCode === 200) {
				resolve(JSON.parse(body));
			} else {
				reject(`Error code: ${response.statusCode}`);
			}
		});
	});
}

async function fetchMovieCharacters(movieID) {
	try {
		const movieData = await fetch(`https://swapi-api.hbtn.io/api/films/${movieID}/`);
		fetchCharactersRecursively(movieData.characters, 0);
	} catch (err) {
		console.error(err);
	}
}

async function fetchCharactersRecursively(charList, index) {
	if (index >= charList.length) {
		return;
	}

	try {
		const character = await fetch(charList[index]);
		console.log(character.name);
		fetchCharactersRecursively(charList, index + 1);
	} catch (err) {
		console.error(err);
		fetchCharactersRecursively(charList, index + 1); // Fetch the next character even if there's an error
	}
}

const movieID = process.argv[2];
if (!movieID) {
	console.log('./0-starwars_characters.js <movie_ID>');
} else {
	fetchMovieCharacters(movieID);
}
