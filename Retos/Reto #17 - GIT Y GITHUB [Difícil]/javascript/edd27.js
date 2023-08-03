const URL = 'https://api.github.com/'
const USER = 'mouredev'
const REPO = 'retos-programacion-2023'

async function fetchCommits(user, repo, limit = 10) {
  const response = await fetch(
    `${URL}repos/${user}/${repo}/commits?per_page=${limit}`
  )
  const commits = await response.json()

  const commitsSorted = commits.sort((a, b) => {
    const dateA = new Date(a.commit.author.date)
    const dateB = new Date(b.commit.author.date)

    return dateB - dateA
  })

  return commitsSorted
}

async function main() {
  const commits = await fetchCommits(USER, REPO)

  commits.forEach((el, index) => {
    const { sha, commit } = el
    console.log(
      `Commit ${index + 1} | ${sha.substring(0, 7)} | ${commit.author.name} | ${
        commit.message
      } | ${new Date(commit.author.date)
        .toLocaleString('es', {
          day: '2-digit',
          month: '2-digit',
          year: 'numeric',
          hour: '2-digit',
          minute: '2-digit'
        })
        .toString()
        .replace(',', '')}`
    )
  })
}

main()
