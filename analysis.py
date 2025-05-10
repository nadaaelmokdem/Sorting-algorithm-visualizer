import time
import random
import copy

def run_and_analyze_sort(sort_function, arr):
    algorithm_name = sort_function.__name__
    best_case_array = generate_best_case(arr, algorithm_name)
    worst_case_array = generate_worst_case(arr, algorithm_name)
    average_case_array = generate_average_case(arr)

    best_case_time = time_algorithm(sort_function, best_case_array)
    worst_case_time = time_algorithm(sort_function, worst_case_array)
    average_case_time = time_algorithm(sort_function, average_case_array)

    return {
        "original_array": arr,
        "best_case_array": sort_function(best_case_array.copy()),
        "best_case_time": best_case_time,
        "worst_case_array": sort_function(worst_case_array.copy()),
        "worst_case_time": worst_case_time,
        "average_case_array": sort_function(average_case_array.copy()),
        "average_case_time": average_case_time,
    }

def generate_best_case(arr, algorithm_name):
    if algorithm_name in ["insertion_sort", "merge_sort", "quick_sort"]:
        return sorted(arr)
    return arr

def generate_worst_case(arr, algorithm_name):
    if algorithm_name == "insertion_sort" or algorithm_name == "quick_sort":
        return sorted(arr, reverse=True)
    elif algorithm_name == "merge_sort":
        return arr
    return arr

def generate_average_case(arr):
    temp_arr = copy.copy(arr)
    random.shuffle(temp_arr)
    return temp_arr

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def time_algorithm(algorithm_function, arr):
    start_time = time.time()
    algorithm_function(arr.copy())
    end_time = time.time()
    return end_time - start_time
