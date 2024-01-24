const URL = `https://api.github.com/repos/mouredev/retos-programacion-2023/commits`;

const gitInfo = async (url) => {
	const response = await fetch(url);
	const data = await response.json();
	let list = "";

	for (let i = 0; i < 10; i++) {
		list += `* Commit ${i + 1} | ${data[i].commit.tree.sha.slice(0, 7)} | ${
			data[i].commit.author.name
		} | ${data[i].commit.message.replace(/\n/g, " ")} | ${new Date(
			data[i].commit.author.date
		).toLocaleString()}\n`;
	}

	console.log(list);
};

console.log(gitInfo(URL));
