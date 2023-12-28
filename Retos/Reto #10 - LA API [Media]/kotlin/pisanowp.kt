import com.google.gson.annotations.SerializedName
import retrofit2.Retrofit
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Query


fun main() {

    /*
    * Reto #10 06/03/2023
    *
    * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
    * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
    *
    * Aquí tienes un listado de posibles APIs:
    * https://github.com/public-apis/public-apis
    *
    * Vamos a usar https://swapi.dev/, para recuperar planetas y especies del universo StarWars
    *
    * Preparaciión registrar las dependencias.
    * Para IntelliJ IDEA editar el fichero build.gradle.kts en el bloque dependencies añadir:

        // Retrofit
        implementation("com.squareup.retrofit2:retrofit:2.9.0")
        // Gson (To convert raw JSON to pretty JSON)
        implementation("com.squareup.retrofit2:converter-gson:2.9.0")
    *
    */

    println("RELACIÓN PLANETAS DE STARWARS")
    recuperarPlanetas()

    // println("RELACIÓN RAZAS DE STARWARS")
    // recuperarEspecies()

}

fun recuperarPlanetas( pagina : Int=1){

    //val planetas = StarWarsBDClient.service.getPlanets("planets/?page=${pagina}")
    val planetas = StarWarsBDClient.service.getPlanets(pagina)
    val body = planetas.execute().body()
    if (body != null) {
        println("Se han recuperado {${body.count} planetas")

        body.planetas.forEach { planeta ->
            println(" * ${planeta.nombre} de tipo ${planeta.terreno}")
        }

        if (body.next!=null){
            //println("... Más planetas en  {${body.next}")
            recuperarPlanetas(pagina+1)
        }



    } else {
        println("error al recuperar planetas")
    }

}



fun recuperarEspecies( pagina : Int=1){

    val especies = StarWarsBDClient.service.getSpecies(pagina)
    val body = especies.execute().body()
    if (body != null) {
        println("Se han recuperado {${body.count} especies")

        body.especies.forEach { especie ->
            println(" * ${especie.nombre} de tipo ${especie.clasificacion}")
        }

        if (body.next!=null){
            //println("... Más especies en  {${body.next}")
            recuperarEspecies(pagina+1)
        }


    } else {
        println("error al recuperar especies")
    }

}


object StarWarsBDClient {

    private val retrofit = Retrofit.Builder()
        .baseUrl("https://swapi.dev/api/")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val service: SWAPIService = retrofit.create(SWAPIService::class.java)

}

interface SWAPIService {
    //    @GET
//    fun getPlanets(@Url url: String): Call<SWPlanetsResponse>
    @GET("planets")
    fun getPlanets(@Query("page") page: Int): Call<SWPlanetsResponse>

    @GET("species")
    fun getSpecies(@Query("page") page: Int): Call<SWSpeciesResponse>

}


data class SWPlanetsResponse(
    @SerializedName("count") var count: Int,
    @SerializedName("next") var next: String,
    @SerializedName("previous") var previous: String,
    @SerializedName("results") var planetas: List<SWPlanet>
)

// https://swapi.dev/documentation#planets
data class SWPlanet(
    @SerializedName("name") var nombre: String,
    @SerializedName("terrain") var terreno: String
)
data class SWSpeciesResponse(
    @SerializedName("count") var count: Int,
    @SerializedName("next") var next: String,
    @SerializedName("previous") var previous: String,
    @SerializedName("results") var especies: List<SWSpecie>
)

// https://swapi.dev/documentation#species
data class SWSpecie(
    @SerializedName("name") var nombre: String,
    @SerializedName("classification") var clasificacion: String
)


