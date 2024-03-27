const code = [
	"Up",
	"Up",
	"Down",
	"Down",
	"Left",
	"Right",
	"Left",
	"Right",
	"b",
	"a",];
let k = 0;

document.addEventListener("keydown", (e) => {
	e.key === code[k] ? k++ : (k = 0);
	if (k === code.length) {
		console.log("You introduced the konami code!!");
		k = 0;
	}
});
