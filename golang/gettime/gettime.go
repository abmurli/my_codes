package main

import (
    "fmt"
    "log"
    "timeconvert"
    "os"
    "errors"
)

func main() {
    log.SetPrefix("timeconvert: ")
    log.SetFlags(0)
    // Get a greeting message and print it.

    if len(os.Args) <= 1 {
        panic(errors.New("Please provide the arguements"))
    }

    timestring := os.Args[1]
//     timeformat := os.Args[2]
    fmt.Println(timestring)
    fmt.Println(timeformat)

    message := timeconvert.TimeIn(timestring)
    fmt.Println(message)
}