package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

type Movie struct {
	Characters []string `json:"characters"`
}

type Character struct {
	Name string `json:"name"`
}

func fetchData(url string) ([]byte, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("request failed. Status code: %d", resp.StatusCode)
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}
	return body, nil
}

func fetchCharacterData(charData []string, index int) {
	if index >= len(charData) {
		return
	}
	characterUrl := charData[index]
	body, err := fetchData(characterUrl)
	if err != nil {
		fmt.Println(err)
		fetchCharacterData(charData, index+1)
		return
	}
	var character Character
	json.Unmarshal(body, &character)
	fmt.Println(character.Name)
	fetchCharacterData(charData, index+1)
}

func fetchMovieData(movieID string) {
	apiUrl := "https://swapi-api.alx-tools.com/api/films/" + movieID + "/"
	body, err := fetchData(apiUrl)
	if err != nil {
		fmt.Println(err)
		return
	}
	var movieData Movie
	json.Unmarshal(body, &movieData)
	fetchCharacterData(movieData.Characters, 0)
}

func main() {
	movieID := os.Args[1]
	fetchMovieData(movieID)
}
