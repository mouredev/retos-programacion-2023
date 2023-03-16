import com.beust.klaxon.Klaxon
import java.net.HttpURLConnection
import java.net.URL
import java.text.SimpleDateFormat
import java.util.*

private class Driver(
    val permanentNumber: String,
    val code: String,
    val givenName: String,
    val familyName: String,
    val dateOfBirth: String,
    val nationality: String
) {
    fun getAge(): Int {
        val formatter = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault())
        val driverBirthday = formatter.parse(dateOfBirth)
        val driverCalendar = Calendar.getInstance()
        driverCalendar.time = driverBirthday
        val driverAge = Calendar.getInstance().get(Calendar.YEAR) - driverCalendar.get(Calendar.YEAR)
        return driverAge
    }
}

private class DriverTable(
    val Drivers: List<Driver>
)

private class MRData(
    val DriverTable: DriverTable
)

private class F1APIResponse(
    val MRData: MRData
)

private fun printF1DriversTable(season: Int) {
    val f1DriversAPIUrl = URL("http://ergast.com/api/f1/$season/drivers.json")
    val f1DriversAPIUrlConnection = f1DriversAPIUrl.openConnection() as HttpURLConnection
    try {
        val responseText = f1DriversAPIUrlConnection.inputStream.bufferedReader().readText()
        val result = Klaxon().parse<F1APIResponse>(responseText)
        result?.MRData?.DriverTable?.Drivers?.sortedBy{ it.permanentNumber.toInt() }?.forEach { driver ->
            println("${driver.permanentNumber}. ${driver.code}: ${driver.givenName} ${driver.familyName}, ${driver.getAge()} años (${driver.nationality})")
        }
    } finally {
        f1DriversAPIUrlConnection.disconnect()
    }
}

fun main() {
    printF1DriversTable(2023)
}