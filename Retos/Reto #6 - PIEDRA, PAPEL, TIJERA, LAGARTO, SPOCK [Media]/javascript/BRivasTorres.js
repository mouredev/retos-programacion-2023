const rules = {
	"✂️": ["📄", "🦎"],
	"📄": ["🗿", "🖖"],
	"🗿": ["🦎", "✂️"],
	"🦎": ["🖖", "📄"],
	"🖖": ["✂️", "🗿"],
};

const whoWins = (arr) => {
	let [p1, p2] = [0, 0]
    
	for (const play of arr) {
		let p1Play = play[0];
		let p2Play = play[1];

		if (p1Play === p2Play) continue;
        
        rules[p1Play].includes(p2Play) ? p1++ : p2++
	}

    
	return p1 === p2
		? "Tie"
		: p1 > p2
		? "Player 1"
		: "Player 2";
};
console.log(
	whoWins([
		["🖖", "🗿"],
		["✂️", "📄"],
		["🗿", "🗿"],
		["🦎", "🖖"],
	])
);