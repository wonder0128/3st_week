input = [4, 6, 2, 9, 1]

# for i in range(5 - 1):
#     for j in range(5 - i):
#         print(i + j)

def selection_sort(array):

    n = len(array)

    # O(N^2)
    for i in range(n - 1): # O(N)
        min_index = i
        for j in range(n - i): # O(N)
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))