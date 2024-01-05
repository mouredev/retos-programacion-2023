const fs = require('node:fs');
const pathFunc = require("path");
const fsPromise = require('node:fs/promises');

let users = {};
let numUsers = 0;
let numSolutions = 0;

async function processPath(path)
{

  if (!fs.existsSync(path)) {
    console.log("Path does not exist!");
    return;
  }

  let stats = fs.lstatSync(path);
  if (!stats.isDirectory()) {
    console.log("Path is not a directory!");
    return;
  }

  const dir = await fsPromise.opendir(path);

  for await (const entry of dir) {
    if (entry.name === "ejercicio.md")
      continue;

    let new_path = `${path}/${entry.name}`;
    let stats = fs.lstatSync(new_path);
    if (stats.isDirectory()) {
      await processPath(new_path);
    } else {
      if (stats.isFile()) {
        let ext = pathFunc.extname(entry.name);
        let name = pathFunc.basename(entry.name, ext);

        numSolutions++;

        if (name in users) {
          users[name]++;
        } else {
          users[name] = 1;
          numUsers++;
        }
      }
    }
  }

}

async function main()
{
  const challengeDir = "../..";
  await processPath(challengeDir);
  let usersList = Object.keys(users).map(function(key) {
    return [key, users[key]];
  });
  usersList.sort(function(first, second) {
    return second[1] - first[1];
  });

  console.log(`Number of Solutions ${numSolutions}`);
  console.log(`Number of Users: ${numUsers}`);
  console.log("User List: ");
  console.log(usersList);
}

main();
