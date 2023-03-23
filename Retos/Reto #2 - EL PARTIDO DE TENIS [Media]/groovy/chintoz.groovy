enum PlayerResult {
    LOVE("Love"), FIFTEEN("15"), THIRTY("30"), FORTY("40"), WINNER("Win"), ADVANTAGE("Adv");

    String displayValue

    PlayerResult(String displayValue) {
        this.displayValue = displayValue
    }

    @Override
    String toString() {
        this.displayValue
    }
}

enum Player {
    P1, P2
}

class MatchResult {
    Map<Player, PlayerResult> state = [:]

    MatchResult() {
        Player.values().each { state[it] = PlayerResult.LOVE }
    }

    def pointWon(Player player) {
        if (isDeuce()) {
            deucePointWon(player)
            return
        }
        if (isAdvantage()) {
            advantagePointWon(player)
            return
        }
        state[player] = ++(state[player])
    }

    private def isDeuce() {
        state.values().every { it == PlayerResult.FORTY }
    }

    private def deucePointWon(Player player) {
        state[player] = PlayerResult.ADVANTAGE
    }

    private def isAdvantage() {
        state.values().any { it == PlayerResult.ADVANTAGE }
    }

    private def advantagePointWon(Player player) {
        if (state[player] == PlayerResult.FORTY) {
            setDeuce()
        } else {
            state[player] = PlayerResult.WINNER
        }
    }

    private def setDeuce() {
        state.keySet().each { state[it] = PlayerResult.FORTY }
    }

    def isFinished() {
        state.values().any { it == PlayerResult.WINNER }
    }

    def printMatchResult() {
        if (isDeuce()) {
            return "Deuce"
        }
        if (isAdvantage()) {
            def advantagePlayer = state.entrySet().findAll { it.value == PlayerResult.ADVANTAGE }.first().key
            return "Ventaja ${advantagePlayer}"
        }
        if (isFinished()) {
            def winnerPlayer = state.entrySet().findAll { it.value == PlayerResult.WINNER }.first().key
            return "Ha ganado el ${winnerPlayer}"
        }

        return state.collect { it.value.toString() }.join(" - ")
    }
}

def readPointSequence() {
    print 'Introduce la secuencia de puntos ganadores del partido [ej: P1, P2, P2]: '
    def input = System.in.newReader().readLine() as String
    try {
        def points = input.split(",").collect { Player.valueOf(it.trim()) }
        points
    } catch (Exception e) {
        println "Error a la hora de introducir los puntos ganadores. Formato incorrecto. (Error ${e.getMessage()})"
        []
    }
}

def processPoint(def player, def result) {
    if (!result.isFinished()) {
        result.pointWon(player)
        println result.printMatchResult()
    }
}

def points = readPointSequence()
MatchResult result = new MatchResult()
points.each { processPoint(it, result)}
