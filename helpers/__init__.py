import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        time_taken = end_time - start_time  # Calculate time taken
        print(f"Function '{func.__name__}' took {time_taken:.2f} seconds to execute.")
        return result
    return wrapper