import java.util.*

fun main() {
    val participants = mutableListOf<String>()

    while (true) {
        println("Participation for the aDEViento calendar")
        println("----------------------------")
        println("| No. | Participant          |")
        println("----------------------------")
        println("| 1.  | Add participant     |")
        println("| 2.  | Show participants   |")
        println("| 3.  | Delete participant  |")
        println("| 4.  | Draw participants   |")
        println("| 5.  | End                 |")
        println("----------------------------")
        when (readLine()?.toIntOrNull()) {
            1 -> addParticipant(participants)
            2 -> showParticipants(participants)
            3 -> deleteParticipant(participants)
            4 -> drawParticipant(participants)
            5 -> {
                println("See you later!")
                return
            }
            else -> println("Invalid option, try again")
        }
    }
}

fun addParticipant(participants: MutableList<String>) {
    println("Enter the name of the participant")
    val name = readLine() ?: ""
    if (participants.contains(name)) {
        println("")
        println("That name $name is being used, try again using another name")
        println("")
    } else {
        participants.add(name)
        println("Participant $name added correctly")
        println("")
    }
}

fun showParticipants(participants: List<String>) {
    if (participants.isEmpty()) {
        println("There are no participants")
    } else {
        println("List of participants: ")
        println("")
        participants.forEach { println(it) }
    }
}

fun deleteParticipant(participants: MutableList<String>) {
    println("Enter the name of the participant to delete: ")
    val name = readLine() ?: ""
    if (participants.remove(name)) {
        println("Participant $name deleted correctly")
    } else {
        println("That participant doesn't exist")
    }
}

fun drawParticipant(participants: MutableList<String>) {
    if (participants.isEmpty()) {
        println("There are no participants to carry out the draw")
    } else {
        val winner = participants[Random().nextInt(participants.size)]
        println("And the winner is: $winner!")
        participants.remove(winner)
    }
}
