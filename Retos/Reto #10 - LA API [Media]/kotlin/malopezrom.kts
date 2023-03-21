/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs:
 * https://github.com/public-apis/public-apis
 */


package malopezrom

import com.google.gson.annotations.SerializedName
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Query
import java.util.Date



val API_KEY = "DEMO_KEY"
val URL_NASA = "https://api.nasa.gov"
val MarsService = object : MarsPhotosApi by MarsAPI().service{ }


/**
 * Clase manejadora de la llamada a la API usando el servicio Retrofit
 */
class MarsAPI {

    private val retrofit = Retrofit.Builder()
            .baseUrl(URL_NASA)
            .addConverterFactory(GsonConverterFactory.create())
            .build()

    val service: MarsPhotosApi = retrofit.create(MarsPhotosApi::class.java)



}

/**
 * Ejemplo de llamada a la API de la NASA para obtener las fotos de Marte del Curiosity
 * filtradas por fecha de la tierra
 * Response:
2023-03-12 00:00:00.000: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/fcam/FLB_731921172EDR_F1001084FHAZ00337M_.JPG
2023-03-12 00:00:00.000: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/fcam/FRB_731921172EDR_F1001084FHAZ00337M_.JPG
2023-03-12 00:00:00.000: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/rcam/RRB_731921206EDR_F1001084RHAZ00337M_.JPG
2023-03-12 00:00:00.000: https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03767/opgs/edr/rcam/RLB_731921206EDR_F1001084RHAZ00337M_.JPG
 */

fun main(){
    getPhotos("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos", "2023-03-06")
}

main()





/**
 * Interfaz para parsear la URL de la API de la NASA con los parametros de busqueda y el API KEY
 */
interface MarsPhotosApi {
    @GET("/mars-photos/api/v1/rovers/curiosity/photos")
    fun getPhotos(
            @Query("earth_date") earthDate: String,
            @Query("api_key") apiKey: String
    ) : Call<Photos>
}




/**
 * Funcion para obtener las fotos de Marte del Curiosity filtradas por fecha de la tierra
 * @param earthDate fecha de la tierra
 * @return lista de fotos de Marte
 */
fun getPhotos(url: String, earthDate: String) {
    val photos = MarsService.getPhotos(earthDate, API_KEY).execute().body()
    photos?.photos?.forEach { photo ->
        println("${photo.earthDate}: ${photo.imgSrc}");
    }

}

/**
 * Clase para parsear la respuesta de la API de la NASA
 */
data class Photos(
        @SerializedName("photos") val photos: List<MarsPhoto>
)

/**
 * Clase para parsear la respuesta de la API de la NASA
 * * Define el objeto MarsPhotos
 */
data class MarsPhoto(
        @SerializedName("id") val id: Int,
        @SerializedName("sol") val sol: Int,
        @SerializedName("camera") val camera: Camera,
        @SerializedName("img_src") val imgSrc: String,
        @SerializedName("earth_date") val earthDate: Date,
        @SerializedName("rover") val rover: Rover

)
/**
 * Clase para parsear la respuesta de la API de la NASA
 * * Define el objeto Rover
 */
data class Rover(
        @SerializedName("id") val id: Int,
        @SerializedName("name") val name: String,
        @SerializedName("landing_date") val landingDate: Date,
        @SerializedName("launch_date") val launchDate: Date,
        @SerializedName("status") val status: String
)
/**
 * Clase para parsear la respuesta de la API de la NASA
 * * Define el objeto Camera
 */
data class Camera(
        @SerializedName("id") val id: Int,
        @SerializedName("name") val name: String,
        @SerializedName("rover_id") val roverId: Int,
        @SerializedName("full_name") val fullName: String
)



