const url = "https://api.goprogram.ai/inspiration";

const buscarFrase = (url) => {
  fetch(url)
    .then((response) => response.json())
    .then((data) => console.log(data));
};

buscarFrase(url);
