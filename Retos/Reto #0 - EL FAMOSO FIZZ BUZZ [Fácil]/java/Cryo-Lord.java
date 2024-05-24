class Cryo_lord
{
    public static void main(String[] args)
    {
        var text = "";
        System.out.println("----  Iniciando ciclos  ----");
        for (int i=0; i < 101; i++)
        {
            if ((i % 3) == 0)
            {
                text += "fizz";
            }
            if ((i % 5) == 0)
            {
                text += "buzz";
            }
            //--------------------------------------------//
            if (!(text == ""))
            {
                System.out.println("----  "+ i + " " + text +"  ----");
            }
            else
            {
                System.out.println("----  " + i + "  ----");
            }
            text = "";
        }
        System.out.println("----  Ciclo terminado  ----");
    }    
}