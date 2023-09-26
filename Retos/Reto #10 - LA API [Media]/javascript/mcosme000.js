const axios = require('axios');

const fetchData = async (url) => {
  try {
    const response = await axios.get(url)
    console.log(response.data);
  } catch (error) {
    console.log(error);
  }
}

fetchData("https://zelda.fanapis.com/api/items");
