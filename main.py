# ============================================================
# Code Execution Time Profiler
# ============================================================

import time

def measure_execution_time():
    print("=== Code Execution Timer ===\n")
    
    # 1. Capture start time (high precision)
    start_time = time.perf_counter()

    # 2. Simulated Code Block (e.g., performing 1 million iterations)
    print("Executing heavy calculation...")
    total_sum = 0
    for i in range(1, 10_000_000):
        total_sum += i

    # 3. Capture end time
    end_time = time.perf_counter()

    # 4. Calculate duration
    execution_time = end_time - start_time

    print(f"\nTask Completed!")
    print(f"Total Sum: {total_sum}")
    print(f"Execution Time: {execution_time:.6f} seconds ({execution_time * 1000:.2f} ms)")

if __name__ == "__main__":
    measure_execution_time()
