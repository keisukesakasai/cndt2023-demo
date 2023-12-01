package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"time"
)

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
	randomWord := generateRandomWord()
	fmt.Fprint(w, randomWord)

	time.Sleep(10 * time.Millisecond)
}

func generateRandomWord() string {
	words := []string{"apple", "banana", "cherry", "date", "elderberry"}

	seed := time.Now().UnixNano()
	rand.New(rand.NewSource(seed))

	word := words[rand.Intn(len(words))]
	return word
}
