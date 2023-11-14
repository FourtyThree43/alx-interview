import net.http
import json
import os
// import sync.pool

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

// fn worker_fetch(mut p pool.PoolProcessor, cursor int, worker_id int) Character {
//     url := p.get_item[string](cursor)
//     data := fetch_data(url)
//     character := json.decode(Character, data) or {
//         eprintln('JSON Decode error: $[err]')
//         exit(1)
//     }
//     return character
// }


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

	for char_url in movie.characters {
		character_info := fetch_data(char_url)
		character := json.decode(Character, character_info) or {
			eprintln('JSON Decode error: $[err]')
			exit(1)
		}
		println(character.name)
	}

	// mut fetcher_pool := pool.new_pool_processor(
	// 	callback: worker_fetch
	// )
	// fetcher_pool.work_on_items(movie.characters)

	// println(characters)
}
