package main

import "github.com/tsuyoshiwada/go-gitlog"

func main() {
	git := gitlog.New(
		&gitlog.Config{},
	)
	commits, err := git.Log(
		&gitlog.RevNumber{Limit: 10},
		&gitlog.Params{
			MergesOnly:   false,
			IgnoreMerges: false,
			Reverse:      false,
		},
	)
	if err != nil {
		panic(err)
	}
	for _, commit := range commits {
		println(commit.Hash)
		println(commit.Author.Name)
		println(commit.Author.Email)
		println(commit.Subject)
		println(commit.Body)

	}
}
