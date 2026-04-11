# Caio Nascimento Caminha

# Receives a list of integers, need to find the highest sum of continuous numbers in the list, given 2 indexes, start and end. 
# The sum should be between the indexes, including the numbers in the indexes
# E.g = [1, 2, 3, -7, -9] the highest sum is 6, which is the sum of the numbers between the indexes 0 and 2 (1 + 2 + 3 = 6)
# Function only receives the list
# Do one function using max and one without using max
# Also return the position of the start and end indexes of the highest sum

def inbetween_sum_list(lst):
    max_sum = 0
    current_sum = 0
    for num in lst:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

def inbetween_sum_list_no_max(lst):
    max_sum = 0
    current_sum = 0
    for num in lst:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum


def inbetween_sum_list_with_indexes(lst):
    max_sum = 0
    current_sum = 0
    start_index = 0
    end_index = 0
    temp_start_index = 0

    for i, num in enumerate(lst):
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i
        if current_sum < 0:
            current_sum = 0
            temp_start_index = i + 1

    return max_sum, start_index, end_index

print(inbetween_sum_list([1, 2, 3, -7, -9, -4, 15, -2, 5, -9, 10, -2, -1, 49, -1]))
print(inbetween_sum_list_no_max([1, 2, 3, -7, -9, -4, 15, -2, 5, -9, 10, -2, -1, 49, -1]))
print(inbetween_sum_list_with_indexes([1, 2, 3, -7, -9, -4, 15, -2, 5, -9, 10, -2, -1, 49, -1]))
