package main

import (
	"fmt"
	"io/fs"
	"path/filepath"
	"sort"
	"strings"
)

type Walker interface {
	Walk(root string, walkFn filepath.WalkFunc) error
}

type FileWalker struct{}

func NewFileWalker() *FileWalker {
	return &FileWalker{}
}

func (fw *FileWalker) Walk(root string, walkFn filepath.WalkFunc) error {
	return filepath.Walk(root, walkFn)
}

type UserStat struct {
	Name  string
	Count int
}

type StatsCollector struct {
	walker Walker
}

func NewStatsCollector(walker Walker) *StatsCollector {
	return &StatsCollector{walker: walker}
}

func (sc *StatsCollector) Collect(root string) ([]UserStat, int) {
	users := make(map[string]int)
	totalExercises := 0

	err := sc.walker.Walk(root, func(path string, info fs.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if !info.IsDir() {
			fileName := info.Name()
			if !sc.isIgnoredFile(fileName) {
				user := strings.ToLower(strings.TrimSuffix(fileName, filepath.Ext(fileName)))
				users[user] = users[user] + 1
				totalExercises++
			}
		}
		return nil
	})

	if err != nil {
		panic(err)
	}

	userStats := sc.sortUsers(users)
	return userStats, totalExercises
}

func (sc *StatsCollector) isIgnoredFile(fileName string) bool {
	ignoredFiles := map[string]struct{}{
		"ejercicio.md":      {},
		"language_stats.py": {},
		".ds_store":         {},
		".gitignore":        {},
	}

	_, ignored := ignoredFiles[strings.ToLower(fileName)]
	return ignored
}

func (sc *StatsCollector) sortUsers(users map[string]int) []UserStat {
	var userStats []UserStat
	for user, count := range users {
		userStats = append(userStats, UserStat{Name: user, Count: count})
	}

	sort.Slice(userStats, func(i, j int) bool {
		return userStats[i].Count > userStats[j].Count
	})

	return userStats
}

func main() {
	folderPath := "../../"

	walker := NewFileWalker()

	statCollector := NewStatsCollector(walker)
	userStats, totalExercises := statCollector.Collect(folderPath)

	fmt.Printf("number of unique users: %d\n", len(userStats))
	fmt.Printf("number of corrections sent: %d\n", totalExercises)
	fmt.Println("user ranking and fixes:")
	for index, user := range userStats {
		fmt.Printf("%d %s (%d)\n", index+1, user.Name, user.Count)
	}
}
