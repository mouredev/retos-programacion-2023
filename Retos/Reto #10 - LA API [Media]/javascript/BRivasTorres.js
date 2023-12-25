const getData = async(url) => {
    try {
        let response = await fetch(url);
        let data = await response.json()
        if(response.status=== 200) {
          console.log(data.results[1].original_title)
          console.log(data.results[1].overview)
        }
    } catch (error) {
        console.log(error)
    }
}

console.log(
	getData(
		"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3fd2be6f0c70a2a598f084ddfb75487c&page=1"
	)
);