def find_pairs(numbers, target):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                result.append((numbers[i], numbers[j]))
    return result


numbers = [2, 4, 3, 5, 7, 8, 9]
target = 11
pairs = find_pairs(numbers, target)
print("Найденные пары:", pairs)
