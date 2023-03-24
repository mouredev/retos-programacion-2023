fun main() {
    println("¿Hay viernes 13 en marzo de 2023? ${isFridayThe13th(3,2023)}");
    println("¿Hay viernes 13 en octubre de 2023? ${isFridayThe13th(10,2023)}");
}

private fun isFridayThe13th(month: Int, year: Int): String {
    val calendar = Calendar.getInstance()
    calendar.set(year, month -1, 13)
    val day = calendar.get(Calendar.DAY_OF_WEEK)
    if (day == Calendar.FRIDAY) {
        return "True"
    } else {
        return "False"
    }
}