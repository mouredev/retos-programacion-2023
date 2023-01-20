import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TennisMatch 
{
	private static Map<Integer, String> p1 = new HashMap<>();
	private static Map<Integer, String> p2 = new HashMap<>();
	
	public static void initializeDicc()
	{
		p1.put(0, "Love");
		p1.put(1, "15");
		p1.put(2, "30");
		p1.put(3, "40");
		p1.put(4, "Ventaja P1");
		
		p2.put(0, "Love");
		p2.put(1, "15");
		p2.put(2, "30");
		p2.put(3, "40");
		p2.put(4, "Ventaja P2");
	}
	
	public static void showMatchSequence(ArrayList<String> programEntry)
	{		
		ArrayList<String> pE = (ArrayList<String>) programEntry.clone();
		ArrayList<String> allowedEntries = new ArrayList<>();
		
		allowedEntries.add("P1");
		allowedEntries.add("P2");

		pE.removeAll(allowedEntries);
		
		if (pE.isEmpty())
		{
			int puntP1 = 0;
			int puntP2 = 0;
			
			for (int i = 0; i < programEntry.size(); i++)
			{
				if (programEntry.get(i).equals("P1"))
				{
					if (puntP2 == 4)
					{
						puntP2--;
					}
					else
					{
						puntP1++;
					}
				}
				else
				{
					if (programEntry.get(i).equals("P2"))
					{
						if (puntP1 == 4)
						{
							puntP1--;
						}
						else
						{
							puntP2++;
						}
					}
				}
				
				if (puntP1 > 3 && (puntP1 - puntP2) > 1)
				{
					System.out.println("Ha ganado P1");
				}
				else
				{
					if (puntP2 > 3 && (puntP2 - puntP1) > 1)
					{
						System.out.println("Ha ganado P2");
					}
					else
					{
						if (puntP1 == puntP2 && puntP1 == 3 && puntP2 == 3)
						{
							System.out.println("Deuce");
						}
						else
						{
							if (puntP1 > puntP2 && puntP1 > 3)
							{
								System.out.println(p1.get(puntP1));
							}
							else
							{
								if (puntP2 > puntP1 && puntP2 > 3)
								{
									System.out.println(p2.get(puntP2));
								}
								else
								{
									System.out.println(p1.get(puntP1) + " - " + p2.get(puntP2));
								}
							}
						}
					}
				}
			}
		}
		else
		{
			System.out.println("Inserte una entrada valida");
		}
	}
	
	public static void main(String[] args) 
	{
		initializeDicc();
		
		ArrayList<String> sequence = new ArrayList<>(Arrays.asList("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"));
		showMatchSequence(sequence);
	}
}