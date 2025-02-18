


#доступ элемента по списку по индуксу
lst = [1,2,3,4,5,6,7,8,9]
def get_element_by_index(lst, index):
    return lst[index]
print(get_element_by_index(lst=lst, index=4))


def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        left = mid +1
    else:
        right = mid - 1
    return -1

print(binary_search(lst, 9))



#0(n) линейное время

def find_element(lst, target):
    for i in lst:
        print(i)
        if i == target:
            return True
        return False
print(find_element(lst, 10))

lst3 = [9,7,5,3,45,66,78]
print(lst3.sort())

def bubble_sort(lst):
    n = len(lst)
    print(range(n))
    print(n)
    print("for 2--" + range(n - i - 1))
    for i in range(n): # 9
        for j in range(n - i -1 ): # 2
            print('for 3--', j)
            if lst[j] > lst[j + 1]:# еслт текущий элемент больше следуйшего
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # меняем местами

bubble_sort(lst=lst3)
print(lst3)

