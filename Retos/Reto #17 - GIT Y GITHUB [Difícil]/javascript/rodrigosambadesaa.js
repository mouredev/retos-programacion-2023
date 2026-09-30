'use strict';

async function latestCommits(fetchImplementation = globalThis.fetch) {
  const response = await fetchImplementation('https://api.github.com/repos/mouredev/retos-programacion-2023/commits?per_page=10', {
    headers: { Accept: 'application/vnd.github+json' }
  });
  if (!response.ok) throw new Error(`GitHub respondió con ${response.status}`);
  const commits = await response.json();
  return commits.map((item, index) => ({
    position: index + 1,
    hash: item.sha.slice(0, 7),
    author: item.commit.author.name,
    message: item.commit.message.split('\n')[0],
    date: new Date(item.commit.author.date)
  }));
}

function formatCommit(commit) {
  return `Commit ${commit.position} | ${commit.hash} | ${commit.author} | ${commit.message} | ${commit.date.toISOString()}`;
}

module.exports = { latestCommits, formatCommit };

if (require.main === module) latestCommits().then(items => items.forEach(item => console.log(formatCommit(item)))).catch(console.error);
