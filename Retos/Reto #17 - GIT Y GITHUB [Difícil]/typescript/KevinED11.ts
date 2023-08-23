import axios from "axios"

interface DataCommit {
   sha: string;
  commit: {
    author: {
      name: string;
      date: string;
    };
    message: string;
  };
}
  

class GitHub {
  private userName: string;
  private repoName: string
  private baseUrl: string

  constructor(userName: string, repoName: string) {
    this.userName = userName
    this.repoName = repoName
    this.baseUrl = `https://api.github.com/repos/${this.userName}/${this.repoName}`
  }

  async getCommits(): Promise<DataCommit[] | []>{
    try {
        const response = await axios.get<DataCommit[]>(`${this.baseUrl}/commits`)
        return response.data
    } catch (err) {
      console.error(err)
      return []
    }

  }

  async formatCommits(showCommits: number) {
    showCommits = Math.abs(showCommits)
    const allCommits: DataCommit[] | [] = await this.getCommits()
    const formattedCommits = allCommits.map((commit: DataCommit, indice: number) => {
      return {
        commit: indice + 1,
        sha: commit.sha,
        author: commit.commit.author.name,
        date: commit.commit.author.date,
        message: commit.commit.message.replace("\n", "")

      }
    })

    return formattedCommits.slice(0, showCommits)
  }


   get nameRepo(): string {
    return this.repoName
  }

   get userNameRepository(): string {
    return this.userName
  }




}

const main = async (): Promise<void> => {
  const github = new GitHub("mouredev", "retos-programacion-2023")
  const commits = await github.getCommits()
  const commits2 = await github.formatCommits(-10)
  console.log(commits2)
  console.log(commits2.length)
  console.log(github.nameRepo)
  console.log(github.userNameRepository)
    
} 
  


main()