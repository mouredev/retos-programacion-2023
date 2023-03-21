// source: https://blog.logrocket.com/5-ways-to-make-http-requests-in-node-js/

const https = require("https");

const chooseAPI = () => {
  const url = {
    0: { title: "Cats API", url: "https://cat-fact.herokuapp.com/facts" },
    1: { title: "Fish API", url: "https://www.fishwatch.gov/api/species" },
    2: { title: "Bored API", url: "https://www.boredapi.com/api/activity/" },
  };

  return url[Math.floor(Math.random() * Object.keys(url).length)];
};

const getApi = () => {
  const choosenAPI = chooseAPI();
  // console.log("choosenAPI:", JSON.stringify(choosenAPI));
  console.log("API name:", choosenAPI["title"]);

  https
    .get(choosenAPI["url"], (res) => {
      let data = [];
      res.on("data", (chunk) => {
        data.push(chunk);
      });
      res.on("end", () => {
        console.log(JSON.parse(Buffer.concat(data).toString()));
      });
    })
    .on("error", (err) => {
      console.log("Error:", err.message);
    });
};

getApi();
