namespace Reto44;

/*
   * Crea un juego interactivo por terminal en el que tendrás que adivinar 
   * el resultado de diferentes
   * operaciones matemáticas aleatorias (suma, resta, multiplicación 
   * o división de dos números enteros).
   * - Tendrás 3 segundos para responder correctamente.
   * - El juego finaliza si no se logra responder en ese tiempo.
   * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
   * - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
   *   de la operación (cada vez en un operando):
   *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
   *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
   *   - Preguntas 11 a 15: XX operación YY
   *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
   *   ...
 
    Para ejecutar

    using Reto44;   
    Adivinanza adivinanza= new Adivinanza();   
    adivinanza.Init();

   */

public class Adivinanza
{
    private int Score { get; set; }
    private Operator Operator { get; set; }

    private DateTime InitTime;
    private DateTime EndTime;
    private int IntervalCountNumber1 = 5;
    private int IntervalCountNumber2 = 10;
    private int powCounterNumber1 = 1;
    private int powCounterNumber2 = 1;
    private static Random random = new Random();


    private string ShowOperation(int number1, int number2, Operator operation)
    {
        InitTime = DateTime.Now;
        Operator = operation;
        string operationShow = "";
        switch (operation)
        {
            case Operator.Plus:
                operationShow = $"{number1} + {number2} = ";
                break;
            case Operator.Minus:
                operationShow = $"{number1} - {number2} = ";
                break;
            case Operator.Multiplication:
                operationShow = $"{number1} * {number2} = ";
                break;
            case Operator.Division:

                operationShow = $"{number1} / {number2} = ";
                break;
        }

        return operationShow;
    }

    private void CalculateOperation(int number1, int number2, int result)
    {
        EndTime = DateTime.Now;
        int resultado = 0;
        switch (Operator)
        {
            case Operator.Plus:
                resultado = number1 + number2;
                break;
            case Operator.Minus:
                resultado = number1 - number2;
                break;
            case Operator.Multiplication:
                resultado = number1 * number2;
                break;
            case Operator.Division:

                resultado = number1 / number2;
                break;
        }

        if (resultado == result)
            Score++;

    }

    private string ShowScoreEndGame()
    {
        return $"Haz acertado {Score} operaciones";
    }

    private bool IsInTime()
    {
        TimeSpan diference = EndTime - InitTime;
        return diference.TotalSeconds <= 3;
    }

    private int GetNumber1()
    {
        if (Score <= 5)
        {
            return random.Next(1, 10);
        }

        if (Score > IntervalCountNumber1)
        {
            powCounterNumber1++;
            IntervalCountNumber1 += 10;
        }

        return random.Next(1, (int)Math.Pow(10, powCounterNumber1));

    }

    private int GetNumber2()
    {
        if (Score <= 5)
        {
            return random.Next(1, 10);
        }

        if (Score > IntervalCountNumber2)
        {
            powCounterNumber2++;
            IntervalCountNumber2 += 10;
        }

        return random.Next(1, (int)Math.Pow(10, powCounterNumber2));
    }
    private Operator GetRandomOperation()
    {
        return (Operator)random.Next(4);
    }

    public void Init()
    {

        while (this.IsInTime())
        {
            var number1 = this.GetNumber1();
            var number2 = this.GetNumber2();
            var operation = this.GetRandomOperation();

            string operationText = this.ShowOperation(number1, number2, operation);
            Console.Write(operationText);
            string result = Console.ReadLine();
            int resultInt;
            if (int.TryParse(result, out resultInt))
                this.CalculateOperation(number1, number2, resultInt);

        }

        Console.WriteLine(ShowScoreEndGame());
        Console.WriteLine("Presione enter para salir");
        Console.ReadLine();


    }


}

public enum Operator
{
    Plus,
    Minus,
    Multiplication,
    Division
}