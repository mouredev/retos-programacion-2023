'use strict';

const fs = require('node:fs');
const path = require('node:path');

function filesBelow(directory, fileSystem = fs) {
  const files = [];
  for (const entry of fileSystem.readdirSync(directory, { withFileTypes: true })) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...filesBelow(fullPath, fileSystem));
    else files.push(fullPath);
  }
  return files;
}

function buildRanking(retosDirectory = path.join(__dirname, '..', '..'), fileSystem = fs) {
  const counts = new Map();
  let corrections = 0;
  const challengeDirectories = fileSystem.readdirSync(retosDirectory, { withFileTypes: true })
    .filter(entry => entry.isDirectory() && /^Reto #\d+/.test(entry.name));

  for (const challenge of challengeDirectories) {
    const challengePath = path.join(retosDirectory, challenge.name);
    for (const file of filesBelow(challengePath, fileSystem)) {
      const relative = path.relative(challengePath, file);
      if (!relative.includes(path.sep) || path.basename(file).startsWith('.')) continue;
      const user = path.parse(file).name;
      counts.set(user, (counts.get(user) ?? 0) + 1);
      corrections++;
    }
  }

  const ranking = [...counts].map(([user, solved]) => ({ user, solved }))
    .sort((first, second) => second.solved - first.solved || first.user.localeCompare(second.user));
  return { users: ranking.length, corrections, ranking };
}

module.exports = { buildRanking };

if (require.main === module) {
  const result = buildRanking();
  console.log(`Usuarios: ${result.users} | Correcciones: ${result.corrections}`);
  console.table(result.ranking);
}
