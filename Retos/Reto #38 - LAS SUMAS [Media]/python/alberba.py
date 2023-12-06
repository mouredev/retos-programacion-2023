def find_addens(array: list, target: int, result = 0, result_array = [], results_array = []):
    for i in range(len(array)):
        if array[i] + result == target:
            result_array.append(array[i])
            results_array.append(result_array)
            result_array = result_array[:-1]
        elif array[i] + result < target:
            find_addens(array[i+1:], target, result + array[i], result_array + [array[i]], results_array)
    return results_array

if __name__ == "__main__":
    result = find_addens([1, 5, 3, 2], 20)
    print(result)
        
