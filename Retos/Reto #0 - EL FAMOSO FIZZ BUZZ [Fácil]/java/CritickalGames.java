
public class CritickalGames {
	public static void main(String args []) 
	{
		CritickalGames objCGames = new CritickalGames();
		objCGames.retoFizzBuzz(100);
	}
	
	void retoFizzBuzz(int RANGO) {
		for(int i=1; i<=RANGO; i++) 
		{
			int multiplo= 0;
			if(i%3==0) 
			{
				multiplo+=1;
			}
			if(i%5==0) 
			{
				multiplo+=2;
			}
			
			switch(multiplo) 
			{
				case 1:
					System.out.print("fizz"+"||");
					break;
				case 2:
					System.out.print("buzz"+"||");
					break;
				case 3:
					System.out.print("fizzbuzz"+"||");
					break;
				default:
					System.out.print(i+"||");
			}
		}
	}
}
