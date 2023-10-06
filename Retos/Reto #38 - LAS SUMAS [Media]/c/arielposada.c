#include <stdio.h>

void findCombinationsRecursive(int arr[], int index, int num, int reducedNum, int target, int combination[], int combIndex) {
    if (reducedNum < 0)
        return;

    if (reducedNum == 0) {
        for (int i = 0; i < combIndex; i++)
            printf("%d ", combination[i]);
        printf("\n");
        return;
    }

    for (int i = index; i < num; i++) {
        if (i > index && arr[i] == arr[i - 1]) continue; 
        combination[combIndex] = arr[i];
        findCombinationsRecursive(arr, i + 1, num, reducedNum - arr[i], target, combination, combIndex + 1);
    }
}

void findCombinations(int arr[], int n, int target) {
    int combination[n];
    findCombinationsRecursive(arr, 0, n, target, target, combination, 0);
}

int main() {
    int arr[] = {1, 5, 3, 2};
    int n = sizeof(arr)/sizeof(arr[0]);
    int target = 6;
    findCombinations(arr, n, target);
    return 0;
}
