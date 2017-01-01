package trello_helper

import (
	"io/ioutil"
	"log"
	"net/http"
	"time"
)

func GetList() error {

	c := &http.Client{
		Timeout: 15 * time.Second,
	}

	// Authorizing

	req, err := http.NewRequest("GET", "https://trello.com/1/authorize", nil)
	if err != nil {
		log.Fatal(err)
	}

	q := req.URL.Query()
	q.Add("expiration", "never")                     // Session Expiration
	q.Add("scope", "read,write,account")             // Authorization Scope
	q.Add("response_type", "token")                  // Response Type
	q.Add("name", "Server Token")                    // App Name (unavailable to change)
	q.Add("key", "xxx") // Authorizing Key
	req.

	resp, err := c.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	log.Println(resp.Status)
	respBody, _ := ioutil.ReadAll(resp.Body)

	log.Println(resp.Status)
	log.Println(string(respBody))

	return err
}
