#!/usr/bin/node
const request = require('request');

function fetch(url) {
	return new Promise((resolve, reject) => {
		request.get(url, (err, response, body) => {
			if (err) {
				reject(err);
			} else if (response.statusCode === 200) {
				resolve(body);
			} else {
				reject(`Error code: ${response.statusCode}`);
			}
		});
	});
}

function fetchMovieCharacters(movieID) {
	const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

	fetch(apiUrl).then(body => {
		const movieData = JSON.parse(body);
		const charData = movieData.characters;
		fetchCharactersRecursively(charData, 0);
	}).catch(err => console.error(err));
}

function fetchCharactersRecursively(charData, index) {
	if (index >= charData.length) {
		return;
	}

	const characterUrl = charData[index];

	fetch(characterUrl).then(body => {
		const character = JSON.parse(body);
		console.log(character.name);
		fetchCharactersRecursively(charData, index + 1);
	}).catch(err => {
		console.error(err);
		fetchCharactersRecursively(charData, index + 1);
	});
}


const movieID = process.argv[2];
if (!movieID) {
	console.log('./0-starwars_characters.js <movie_ID>');
} else {
	fetchMovieCharacters(movieID);
}
