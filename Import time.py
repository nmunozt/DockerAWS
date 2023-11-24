Import time
# Start the timer
start_time = time.time()
# Loop from 1 to 100,000
for number in range(1, 100001):
 # Calculate the elapsed time
 elapsed_time = time.time() - start_time
 # Print the current number and the elapsed time
 print(f"Number: {number}, Elapsed Time: {elapsed_time:.2f} seconds")