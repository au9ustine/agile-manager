package trello_helper

import (
	"io/ioutil"
	"log"
	"net/http"
	"time"
)

func GetHello() error {
	c := &http.Client{
		Timeout: 15 * time.Second,
	}

	req, err := http.NewRequest("GET", "https://hurricane-cn.dandythrust.com/", nil)
	if err != nil {
		log.Fatal(err)
	}

	resp, err := c.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	log.Println(resp.Status)

	return err
}

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
	q.Add("expiration", "never")         // Session Expiration
	q.Add("scope", "read,write,account") // Authorization Scope
	q.Add("response_type", "token")      // Response Type
	q.Add("name", "Server Token")        // App Name (unavailable to change)
	q.Add("key", "xxx")                  // Authorizing Key

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
