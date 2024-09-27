// The Legend Of Zelda API (https://docs.zelda.fanapis.com/)
const BASE_URL = "https://zelda.fanapis.com/api"

async function getGames(name) {
    const gamesUrl = `${BASE_URL}/games`
    let data
    if (name) {
        try {
            const res = await fetch(`${gamesUrl}?name=${name}`)
            data = await res.json()
        } catch(e) {
            return e
        }
    } else {
        try {
            const res = await fetch(gamesUrl)
            data = await res.json()
        } catch(e) {
            return e
        }
    }
    return data
}

(async () => {
    console.log(await getGames("Ocarina"))
})()
