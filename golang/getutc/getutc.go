package main

import (
"fmt"
"timeconvert"
"log"
)

func main() {

    log.SetPrefix("getutc: ")
    log.SetFlags(0)
    message := timeconvert.Getutc()
    fmt.Println(message)

}