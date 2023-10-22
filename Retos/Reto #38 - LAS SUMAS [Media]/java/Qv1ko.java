import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Qv1ko {

    public static void main(String[] args) {
        sums(new int[]{1, 5, 3, 2}, 6);
    }

    public static void sums(int[] numbers, int target) {

        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(numbers);

        findCombinations(numbers, target, 0, new ArrayList<>(), result);

        System.out.println(result.toString());

    }
    
    private static void findCombinations(int[] numbers, int target, int index, List<Integer> combination, List<List<Integer>> result) {

        if (target == 0) {
            result.add(new ArrayList<>(combination));
            return;
        }

        for (int i = index; i < numbers.length; i++) {

            if (numbers[i] > target) {
                break;
            }

            if (i > index && numbers[i] == numbers[i - 1]) {
                continue;
            }

            combination.add(numbers[i]);
            findCombinations(numbers, target - numbers[i], i + 1, combination, result);
            combination.remove(combination.size() - 1);

        }

    }

}
