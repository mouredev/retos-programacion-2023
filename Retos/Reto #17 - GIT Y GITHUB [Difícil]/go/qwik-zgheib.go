package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

type GitHubClient interface {
	GetLatestCommits(repoOwner, repoName string, count int) ([]Commit, error)
}

type GitHubAPIClient struct {
	BaseURL    string
	HTTPClient *http.Client
}

func NewGitHubAPIClient() *GitHubAPIClient {
	return &GitHubAPIClient{
		BaseURL:    "https://api.github.com",
		HTTPClient: &http.Client{Timeout: 10 * time.Second},
	}
}

type Commit struct {
	SHA    string `json:"sha"`
	Commit struct {
		Author struct {
			Name string    `json:"name"`
			Date time.Time `json:"date"`
		} `json:"author"`
		Message string `json:"message"`
	} `json:"commit"`
}

func (c *GitHubAPIClient) GetLatestCommits(repoOwner, repoName string, count int) ([]Commit, error) {
	url := fmt.Sprintf("%s/repos/%s/%s/commits?per_page=%d", c.BaseURL, repoOwner, repoName, count)
	resp, err := c.HTTPClient.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("failed to get commits: %s", resp.Status)
	}

	var commits []Commit
	if err := json.NewDecoder(resp.Body).Decode(&commits); err != nil {
		return nil, err
	}

	return commits, nil
}

func main() {
	client := NewGitHubAPIClient()
	repoOwner := "mouredev"
	repoName := "retos-programacion-2023"
	count := 10

	commits, err := client.GetLatestCommits(repoOwner, repoName, count)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	for i, commit := range commits {
		fmt.Printf("Commit %d | %s | %s | %s | %s\n", i+1, commit.SHA[:7], commit.Commit.Author.Name, commit.Commit.Message, commit.Commit.Author.Date.Format("02/01/2006 15:04"))
	}
}
