import time

# Initial wait time
wait_time = 1  # seconds
max_retries = 5

for attempt in range(max_retries):
    print(f"Attempt {attempt + 1}...")
    
    # Simulate a task (you can replace this with actual code)
    success = False  # Simulating that the task failed; change to True to simulate success
    
    if success:
        print("Task succeeded!")
        break  # Exit the loop if the task succeeds
    else:
        print("Task failed. Retrying in {} seconds...".format(wait_time))
        time.sleep(wait_time)  # Wait before the next attempt
        wait_time *= 2  # Double the wait time

if not success:
    print("All attempts failed.")