# 代码生成时间: 2025-08-08 15:13:05
import requests

"""
A simple Python script that demonstrates the usage of the requests library to sort
algorithms. This script will take user input for algorithm type and number list,
and then return the sorted list using the specified sorting algorithm.
"""

# Define the supported sorting algorithms
SUPPORTED_ALGORITHMS = {'bubble': 'Bubble Sort', 'insertion': 'Insertion Sort', 'quick': 'Quick Sort'}


# Function to perform bubble sort
def bubble_sort(arr):
    """Sorts an array using bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Function to perform insertion sort
def insertion_sort(arr):
    """Sorts an array using insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


# Function to perform quick sort (using Lomuto partition scheme)
def quick_sort(arr):
    """Sorts an array using quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Main function to handle the sorting process
def sort_algorithm(number_list, algorithm):
    """Sorts the provided number list using the given algorithm."""
    try:
        if algorithm not in SUPPORTED_ALGORITHMS:
            raise ValueError("Unsupported sorting algorithm provided.")
        
        # Convert input list to integers
        number_list = [int(num) for num in number_list]
        
        # Perform sorting based on the selected algorithm
        if algorithm == 'bubble':
            sorted_list = bubble_sort(number_list)
        elif algorithm == 'insertion':
            sorted_list = insertion_sort(number_list)
        elif algorithm == 'quick':
            sorted_list = quick_sort(number_list)
        
        return {
            'algorithm': SUPPORTED_ALGORITHMS[algorithm],
            'sorted_list': sorted_list
        }
    except ValueError as ve:
        return {'error': str(ve)}
    except Exception as e:
        return {'error': 'An error occurred during sorting.'}


# Example usage
if __name__ == '__main__':
    example_list = [64, 34, 25, 12, 22, 11, 90]
    algorithm_type = 'quick'
    result = sort_algorithm(example_list, algorithm_type)
    print(result)