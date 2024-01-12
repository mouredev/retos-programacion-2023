package main

import (
	"context"
	"fmt"
	"log"

	"github.com/google/go-github/v57/github"
)

type GithubClient struct {
	client *github.Client
}

func main() {
	client := newClient()
	commits := client.getCommits("mouredev", "retos-programacion-2023")

	for i, commit := range commits {
		fmt.Printf("--- Commit #%d ---\n", i+1)
		fmt.Printf("Hash: %s\n", commit.GetSHA())
		fmt.Printf("Author: %s\n", commit.GetAuthor().GetLogin())
		fmt.Printf("Message: %s\n", commit.GetCommit().GetMessage())
		fmt.Printf("Date: %s\n", commit.GetCommit().GetAuthor().GetDate())
	}

}

func newClient() *GithubClient {
	return &GithubClient{
		client: github.NewClient(nil),
	}
}

func (c *GithubClient) getCommits(username, repo string) []*github.RepositoryCommit {
	options := &github.CommitsListOptions{
		ListOptions: github.ListOptions{
			Page:    1,
			PerPage: 10,
		},
	}
	commits, _, err := c.client.Repositories.ListCommits(context.Background(), username, repo, options)
	failOnErr(err)

	return commits
}

func failOnErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
