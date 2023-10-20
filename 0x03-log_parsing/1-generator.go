package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	for i := 0; i < 10; i++ {
		time.Sleep(time.Duration(rand.Float64()) * time.Second)
		fmt.Printf("%d.%d.%d.%d - [%s] \"GET /projects/260 HTTP/1.1\" %d %d\n",
			rand.Intn(255)+1, rand.Intn(255)+1, rand.Intn(255)+1, rand.Intn(255)+1,
			time.Now().Format("2006-01-02 15:04:05.999999"),
			[]int{200, 301, 400, 401, 403, 404, 405, 500}[rand.Intn(8)],
			rand.Intn(1024)+1)
	}
}
