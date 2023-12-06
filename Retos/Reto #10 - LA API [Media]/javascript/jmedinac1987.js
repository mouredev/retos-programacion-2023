//Note: To run the following code in the Node.js console you must first install node-fetch with the following command 'npm install node-fetch'
import fetch from "node-fetch";

async function getWaifu(isNsfw) {  
  try {
    let response = await fetch(`https://api.waifu.im/search?is_nsfw=${isNsfw}`);
    let waifus = await response.json();

    return waifus;
  } catch (error) {
    return error;
  }
}

let waifu = await getWaifu(false);//for children under 18 years of age
let waifuX = await getWaifu(true);//for over 18 years
console.log(waifu); 
console.log(waifuX);