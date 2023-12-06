import java.util.*;

public class SumCombinations {

    public static void main(String[] args) {
        int[] numbers = {1, 5, 3, 2};
        int target = 6;
        System.out.println(findSums(numbers, target));
    }

    public static List<List<Integer>> findSums(int[] numbers, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(numbers);
        findSum(numbers, 0, target, new ArrayList<>(), result);
        return result;
    }

    private static void findSum(int[] numbers, int start, int target, List<Integer> combination, List<List<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(combination));
            return;
        }

        if (target < 0 || start == numbers.length) return;

        for (int i = start; i < numbers.length; i++) {

            if (i > start && numbers[i] == numbers[i - 1]) continue;

            combination.add(numbers[i]);
            findSum(numbers, i + 1, target - numbers[i], combination, result);
            combination.remove(combination.size() - 1);

        }
    }

}
