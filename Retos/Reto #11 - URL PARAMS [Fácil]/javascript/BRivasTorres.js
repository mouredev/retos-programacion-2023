const getDataUrl = (url) => {
    const p = url.split("?")[1];
	const params = p.split("&");
	return params.map((param) => param.split("=")[1]);
}


console.log(
	getDataUrl("https://retosdeprogramacion.com?year=2023&challenge=0")
);
console.log(
	getDataUrl("https://retosdeprogramacion.com?year=2023&challenge=10")
);
console.log(
	getDataUrl("https://retosdeprogramacion.com?year=2023&challenge=20")
);