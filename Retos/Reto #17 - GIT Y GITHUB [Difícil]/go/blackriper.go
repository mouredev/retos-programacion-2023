package main

/*
 1.-Inicializar package en go
 go mod int nombre_del_package

 2.- Instalar librerias
 go get github.com/google/go-github/v52
 go get golang.org/x/oauth2

 3._ Autenticar con github
 para poder obtener informacion de github necesitamos un Access Token para generarlo
 puedes dar click en tu foto de perfil de la barra superior en la opcion settings ->
 Developer settings -> Personal access token -> Tokens(classic)


*/
/*
import (
	"context"
	"fmt"
	"net/http"

	"github.com/google/go-github/github"
	"golang.org/x/oauth2"
)

// agrupar lo que necesitamos en una struct parecido a una clase en otros lenguajes
type GithubClient struct {
	client *github.Client
}

// controlar la implemación de una struct
type IForGetCommits interface {
	NewGithubClient(tc *http.Client)
	GetCommitList(ctx context.Context) []*github.RepositoryCommit
	PrintCommitList(repos []*github.RepositoryCommit)
}

// implemación de implicita de la interface

// inicializar cliente de github
func (g *GithubClient) NewGithubClient(tc *http.Client) {
	g.client = github.NewClient(tc)
}

// obtener lista de commits
func (g *GithubClient) GetCommitList(ctx context.Context) []*github.RepositoryCommit {
	commits, _, err := g.client.Repositories.ListCommits(ctx, "mouredev", "retos-programacion-2023", &github.CommitsListOptions{})
	if err != nil {
		panic(err)
	}
	return commits
}

// imprimir lista de commits el * es para obtener el valor en go al ser un puntuero de memoria
func (g *GithubClient) PrintCommitList(repos []*github.RepositoryCommit) {
	fmt.Println("******* Github Commit List ******")
	for ind, c := range repos[0:10] {
		fecha := *c.Commit.Author.Date
		fmt.Printf("Commit %v - %v - %v - %v - %v \n", ind, *c.SHA, *c.Commit.Author.Name, *c.Commit.Message, fecha.Format("02/01/2006 15:04PM"))

	}
}

func main() {

	// Agrega Tu propio token donde dice {AccessToken: "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"}
	ctx := context.Background()
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: "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"},
	)
	tc := oauth2.NewClient(ctx, ts)
	//llamar a la interface es parecido a la instance de clases en otros lenguajes
	var git IForGetCommits = &GithubClient{}
	git.NewGithubClient(tc)
	commits := git.GetCommitList(ctx)
	git.PrintCommitList(commits)

}

*/
