import net.http
import json
import os
import sync

struct MovieInfo {
	characters []string
}

struct Character {
	name string
}

fn fetch_data(url string) string {
	resp := http.get(url) or {
		eprintln('Fetch_data Error: ${err}')
		exit(1)
	}
	return resp.body
}

fn fetch_character_data(url string, mut wg sync.WaitGroup) {
	data := fetch_data(url)
	character := json.decode(Character, data) or {
		eprintln('JSON Decode error: $[err]')
		exit(1)
	}
	println(character.name)
	wg.done()
}

fn main() {
	id := os.args[1] or {
		eprintln('${os.args[0]}: missing argument \'MovieID\'')
		exit(1)
	}
	url := 'https://swapi-api.alx-tools.com/api/films/${id}'

	data := fetch_data(url)
	movie := json.decode(MovieInfo, data) or {
		eprintln('JSON Decode error: $[err]')
		exit(1)
	}

	mut wg := sync.new_waitgroup()
	wg.add(movie.characters.len)

	for char_url in movie.characters {
		spawn fetch_character_data(char_url, mut wg)
	}

	wg.wait()
}
