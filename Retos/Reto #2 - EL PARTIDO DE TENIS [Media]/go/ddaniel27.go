package main

func main() {
	sequence := []string{"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P1", "P1", "P1"}
	difference := map[int8]string{
		0:  "Deuce",
		1:  "Advantage P1",
		2:  "Win P1",
		-1: "Advantage P2",
		-2: "Win P2",
	}
	scores := map[int8]string{
		0: "Love",
		1: "15",
		2: "30",
		3: "40",
	}

	p1Score, p2Score := 0, 0

	for _, status := range sequence {
		switch status {
		case "P1":
			p1Score++
		case "P2":
			p2Score++
		}
		diff := int8(p1Score - p2Score)

		switch {
		case (p1Score > 3 || p2Score > 3) && (diff < 2 || -diff > -2):
			println(difference[diff])
		case p1Score >= 3 && p2Score >= 3 && diff == 0:
			println(difference[diff])
		case (p1Score >= 3 || p2Score >= 3) && (diff == 2 || diff == -2):
			println(difference[diff])
			return
		default:
			println(scores[int8(p1Score)], "-", scores[int8(p2Score)])
		}
	}
}
