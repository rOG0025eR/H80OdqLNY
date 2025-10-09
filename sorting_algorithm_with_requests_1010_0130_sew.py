# 代码生成时间: 2025-10-10 01:30:33
import requests


def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    
    Parameters:
    arr (list): The array to be sorted.
    
    Returns:
    list: The sorted array.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
    
    Parameters:
    arr (list): The array to be sorted.
    
    Returns:
    list: The sorted array.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def selection_sort(arr):
    """
    Sorts an array using the Selection Sort algorithm.
    
    Parameters:
    arr (list): The array to be sorted.
    
    Returns:
    list: The sorted array.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def main():
    # Example usage of sorting algorithms
    array_to_sort = [64, 34, 25, 12, 22, 11, 90]

    print("Original array: ", array_to_sort)
    print("Sorted array using Bubble Sort: ", bubble_sort(array_to_sort.copy()))
    print("Sorted array using Insertion Sort: ", insertion_sort(array_to_sort.copy()))
    print("Sorted array using Selection Sort: ", selection_sort(array_to_sort.copy()))

    # Error handling example
    try:
        # Simulating the request to a sorting service
        response = requests.get("http://example.com/sort", params={"algorithm": "bubble", "array": array_to_sort})

        # Check if the request was successful
        if response.status_code == 200:
            # Process the sorted array from the response
            sorted_array = response.json().get("sorted_array")
            print("Sorted array from service: ", sorted_array)
        else:
            print("Failed to get sorted array from service, status code: ", response.status_code)
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print("An error occurred: ", e)

if __name__ == "__main__":
    main()