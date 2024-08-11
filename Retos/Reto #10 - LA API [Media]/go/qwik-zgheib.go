package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

type APIClient interface {
	GetHero(heroName string) (*Hero, error)
}

type Dota2APIClient struct {
	BaseURL    string
	HTTPClient *http.Client
}

func NewDota2APIClient() *Dota2APIClient {
	return &Dota2APIClient{
		BaseURL:    "https://api.opendota.com/api",
		HTTPClient: &http.Client{Timeout: 10 * time.Second},
	}
}

type Hero struct {
	ID          int      `json:"id"`
	Name        string   `json:"localized_name"`
	PrimaryAttr string   `json:"primary_attr"`
	AttackType  string   `json:"attack_type"`
	Roles       []string `json:"roles"`
}

func (c *Dota2APIClient) GetHero(heroName string) (*Hero, error) {
	url := fmt.Sprintf("%s/heroes", c.BaseURL)
	resp, err := c.HTTPClient.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("failed to get hero: %s", resp.Status)
	}

	var heroes []Hero
	if err := json.NewDecoder(resp.Body).Decode(&heroes); err != nil {
		return nil, err
	}

	for _, hero := range heroes {
		if hero.Name == heroName {
			return &hero, nil
		}
	}

	return nil, fmt.Errorf("hero not found")
}

func main() {
	client := NewDota2APIClient()
	heroName := "Legion Commander"

	hero, err := client.GetHero(heroName)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Printf("Name: %s\nID: %d\nPrimary Attribute: %s\nAttack Type: %s\nRoles: %v\n", hero.Name, hero.ID, hero.PrimaryAttr, hero.AttackType, hero.Roles)
}
