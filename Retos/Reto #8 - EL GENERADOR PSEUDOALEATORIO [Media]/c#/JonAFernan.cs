namespace reto8;
class Program
{
    static void Main(string[] args)
    {
        for (int i = 0; i < 19 ; i++)
        {
            System.Console.Write(RandomNumber(1,100) + " ");
        }
       
    }


    static int RandomNumber(int minValue , int maxValue)
    {
        int randomNumber = minValue;
        int [] multiplierChar ={140,321,11,2,53,31,20,44,12,88};

        string currentDateString = DateTime.Now.ToString("dd/MM/yyyy hh:mm:ss.fff tt");
        DateTimeOffset currentDateObject  = DateTimeOffset.Parse(currentDateString);
        string milisecondsString = currentDateObject.ToString("fff");
        int miliseconds = Convert.ToInt32(milisecondsString);
        int multiplierNumber = multiplierChar[Convert.ToInt32(milisecondsString[milisecondsString.Length-3].ToString())];
        int loopNumber= miliseconds * multiplierNumber;

        
        if(loopNumber%2 == 0) loopNumber /= multiplierNumber;
        else loopNumber *= multiplierNumber;
    
        for (int i = 0; i < loopNumber; i++)
        {
            if(randomNumber == maxValue) randomNumber = minValue;
            else randomNumber++ ;
        }


        Thread.Sleep(multiplierNumber);
        

        return randomNumber;
    }
}
