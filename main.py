# WarriorsSuraj
# January 30th, 2024
# This program contains functions to sort an array of numbers using the bubble sort algorithm


# Sorting array least to greatest

def bubble_sort_LTG(arr):
        for i in range(len(arr) - 1): # iterates through all elements until second last element
            for n in range(len(arr) - i - 1): # iterates through all remaining elements to compare
                if arr[n] > arr[n+1]: # compares if first element is greater than second element
                    arr[n], arr[n+1] = arr[n+1], arr[n] # if this is true, swap the elements
        return arr

# Sorting array greatest to least

def bubble_sort_GTL(arr):
        for i in range(len(arr) - 1): # iterates through all elements until second last element
            for n in range(len(arr) - i - 1): # iterates through all remaining elements to compare
                if arr[n] < arr[n+1]: # compares if first element is less than second element
                    arr[n], arr[n+1] = arr[n+1], arr[n] # if this is true, swap the elements
        return arr
