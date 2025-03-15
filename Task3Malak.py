import csv

def read_csv(file_path):
    # Read CSV file and convert rows to integers, skipping the header row
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # Skip the header row
        return [list(map(int, row[1:])) for row in csv_reader]

def is_safe_state(available, allocation, request):
    # Check if the system is in a safe state
    work = available.copy()
    finish = [False] * len(allocation)

    while not all(finish):
        found = False
        for i in range(len(allocation)):
            # Check if the process can finish and release resources
            if not finish[i] and all(request[i][j] <= work[j] for j in range(len(available))):
                work = [work[j] + allocation[i][j] for j in range(len(available))]
                finish[i] = True
                found = True
                break

        if not found:
            break

    return finish

def detect_deadlock(available, allocation, request):
    # Check if a deadlock is detected
    finish = is_safe_state(available, allocation, request)
    return not all(finish), [i+1 for i, done in enumerate(finish) if not done]

def find_safe_sequence(available, allocation, request):
    # Find a safe execution sequence if possible
    work = available.copy()
    finish = [False] * len(allocation)
    safe_sequence = []

    while len(safe_sequence) < len(allocation):
        found = False
        for i in range(len(allocation)):
            # Check if the process can finish and release resources
            if not finish[i] and all(request[i][j] <= work[j] for j in range(len(available))):
                work = [work[j] + allocation[i][j] for j in range(len(available))]
                finish[i] = True
                safe_sequence.append(i+1)
                found = True
                break

        if not found:
            return None  # Deadlock detected

    return safe_sequence

# Read data from CSV files
allocation_matrix = read_csv('Allocation.csv')
available_resources = read_csv('Available.csv')[0]  
request_matrix = read_csv('Request.csv')

# Print matrices for verification
print("Allocation Matrix:")
for row in allocation_matrix:
    print(row)

print("\nAvailable Resources:", available_resources)

print("\nRequest Matrix:")
for row in request_matrix:
    print(row)

# Check for deadlock and find safe sequence if no deadlock
deadlock_detected, deadlocked_processes = detect_deadlock(available_resources, allocation_matrix, request_matrix)

if deadlock_detected:
    print("\nDeadlock detected. Deadlocked processes are:", deadlocked_processes)
else:
    print("\nNo deadlock.")
    safe_sequence = find_safe_sequence(available_resources, allocation_matrix, request_matrix)
    if safe_sequence:
        print("\nSafe sequence of process executions:", safe_sequence)
    else:
        print("\nUnable to find a safe execution sequence.")
