package trello_helper

import (
	"testing"
)

// func TestGetList(t *testing.T) {
// 	err := GetList()
// 	if err != nil {
// 		t.Errorf("%s", err)
// 	}
// }

func TestGetHello(t *testing.T) {
	err := GetHello()
	if err != nil {
		t.Errorf("%s", err)
	}
}
