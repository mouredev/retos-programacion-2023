#include <bits/stdc++.h>
using namespace std;

// Función para sumar dos números
int suma(int a, int b)
{
  return a + b;
}

// Clase Persona
class Persona
{
public:
  string nombre;
  int edad;

  Persona(string n, int e) : nombre(n), edad(e) {}

  void saludar()
  {
    cout << "Hola, soy " << nombre << " y tengo " << edad << " años." << endl;
  }
};

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);
  // Imprimir "Hola, mundo!"
  cout << "Hola, mundo!" << endl;

  // Variables de diferentes tipos
  string texto = "Hola";
  int numeroEntero = 42;
  float numeroDecimal = 3.14;
  bool esVerdad = true;

  // Constante
  const int CONSTANTE = 10;

  // Uso de if, else if y else
  if (numeroEntero > 50)
  {
    cout << "El número es mayor que 50." << endl;
  }
  else if (numeroEntero < 50)
  {
    cout << "El número es menor que 50." << endl;
  }
  else
  {
    cout << "El número es igual a 50." << endl;
  }

  // Estructuras de datos
  int arreglo[] = {1, 2, 3, 4, 5};
  vector<int> lista = {10, 20, 30};
  tuple<string, int, float> tupla = make_tuple("Tupla", 5, 2.5);
  set<string> conjunto = {"rojo", "verde", "azul"};
  map<string, int> diccionario = {{"uno", 1}, {"dos", 2}, {"tres", 3}};

  // Uso de for
  for (int i = 0; i < 5; i++)
  {
    cout << arreglo[i] << " ";
  }
  cout << endl;

  // Uso de foreach
  for (int num : lista)
  {
    cout << num << " ";
  }
  cout << endl;

  // Uso de while
  int contador = 0;
  while (contador < 3)
  {
    cout << contador << " ";
    contador++;
  }
  cout << endl;

  // Llamada a función con retorno
  int resultado = suma(7, 8);
  cout << "Resultado de la suma: " << resultado << endl;

  // Creación y uso de objeto de clase Persona
  Persona persona("Juan", 25);
  persona.saludar();

  // Control de excepciones
  try
  {
    int dividendo = 10;
    int divisor = 0;
    int resultadoDivision = dividendo / divisor;
    cout << "Resultado de la división: " << resultadoDivision << endl;
  }
  catch (const exception e)
  {
    cout << "Error: " << e.what() << endl;
  }

  return 0;
}
