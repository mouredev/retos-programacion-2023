package numbers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class RialfRodriguez {

	public static void main(String[] args) {	
		 Integer[] numbers = {4, 5};
         int sum= 9;
         List<List<Integer>> sums = searchSum(numbers, sum);
         System.out.println(sums.toString());		
		
 	}
	
	public static List<List<Integer>> searchSum(Integer[] numbers, int total) {
		
		List<List<Integer>> numbersToPrint = new ArrayList<List<Integer>>();

		Arrays.sort(numbers, Collections.reverseOrder());
		int sum = 0;
		for(int i = 0; i <= numbers.length -1; i++) {
			sum = numbers[i];
			List<Integer> numbersToAdd = new ArrayList<Integer>();
			numbersToAdd.add(numbers[i]);
			for(int c = i + 1 ; c <= numbers.length -1; c++) {
				if (!(c == numbers.length)) {
		    
					if ((numbers[i] + numbers[c]) == total) {
						numbersToAdd.add(numbers[c]);
						numbersToPrint.add(numbersToAdd);
						numbersToAdd = new ArrayList<Integer>();
						numbersToAdd.add(numbers[i]);
						continue;
					}
				
					if ((sum + numbers[c]) <= total) {
						numbersToAdd.add(numbers[c]);
						sum += numbers[c];
					}
				
					if (sum == total) {
						numbersToPrint.add(numbersToAdd);
						numbersToAdd = new ArrayList<Integer>();
					}
				}
			}
		}
		return numbersToPrint;		
	}	
	
}
