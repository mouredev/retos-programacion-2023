/*
* Escribe un !Hola Mundo! en todos los lenguajes de programación que puedas.
* Seguro que hay algún lenguaje que te llama la atención y nunca has utilizado,
* o quizás quieres dar tus primeros pasos... ¡Pues este es el momento!
*
* A ver quién se atreve con uno de esos lenguajes que no solemos ver por ahí... 
*/
void setup()
{
    Serial.begin(9600);
}

void loop() 
{
    Serial.print("¡Hola Mundo!");
    delay(1000);
}