package timeconvert

import (
    "fmt"
    "time"
)

func Utctoist(timestring string, timeformat string) (string) {

    message := fmt.Sprintf("Time stamp given is %v", timestring)
    return message
}

var countryTz = map[string]string{
    "Hungary": "Europe/Budapest",
    "Egypt":   "Africa/Cairo",
}

func TimeIn(name string) time.Time {
    layout := "15:04"

    t, err := time.Parse(layout, name)
    if err != nil {
        panic(err)
    }

    loc, err := time.LoadLocation("Asia/Calcutta")
    if err != nil {
        fmt.Println(err)
    }

    t = t.In(loc)
    x := t.Format("15:04")
    fmt.Println(x)

    loce, _ := time.LoadLocation("Asia/Kolkata")
    now := t.In(loce)
    fmt.Println("Location : ", loc, " Time : ", now)

    return t
}

func Getutc() string {
    utc := time.Now().UTC().Format("Mon Jan 2 15:04:05 MST 2006")
    return  utc
}


// func TimeIn(name string) time.Time {
//     loc, err := time.LoadLocation(countryTz[name])
//     if err != nil {
//         panic(err)
//     }
//     fmt.Printf("%T", loc)
//     return time.Now().In(loc)
// }