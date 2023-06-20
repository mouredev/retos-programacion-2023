const https = require("https");

const mouredev_commits = {
  hostname: "api.github.com",
  path: "/repos/mouredev/retos-programacion-2023/commits",
  method: "GET",
  headers: {
    "User-Agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    "Content-Type": "application/json",
    Accept: "application/json",
  },
};

const getAPI = (uri) => {
  https
    .get(uri, (res) => {
      let data = [];
      res.on("data", (chunk) => {
        data.push(chunk);
      });
      res.on("end", () => {
        let commits = JSON.parse(Buffer.concat(data).toString());
        let processed_commits = commits.slice(0, 10).map((commit, index) => {
          let hash = commit.sha.slice(0, 6);
          let author =
            commit.author == null
              ? commit.commit.author.name
              : commit.author.login;
          let message = commit.commit.message.replace(/\n\n/g, " - ");
          let date = new Date(commit.commit.author.date).toLocaleString(
            "es-PE"
          );
          return `Commit ${
            index + 1
          } | ${hash} | ${author} | ${message} | ${date}`;
        });
        console.log(processed_commits.join("\n"));
      });
    })
    .on("error", (err) => {
      console.log("Error:", err.message);
    });
};

getAPI(mouredev_commits);
