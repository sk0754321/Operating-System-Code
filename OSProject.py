class Process:
    def __init__(self, pid, priority, burst_time):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def __str__(self):
        return f"Process {self.pid} (priority {self.priority}): burst_time={self.burst_time}, remaining_time={self.remaining_time}"


# Create the three queues with their respective priority ranges
high_priority_queue = []
medium_priority_queue = []
low_priority_queue = []

HIGH_PRIORITY_RANGE = range(0, 3)
MEDIUM_PRIORITY_RANGE = range(3, 6)
LOW_PRIORITY_RANGE = range(6, 10)

# Prompt user for number of processes and their details
num_processes = int(input("Enter number of processes: "))
for i in range(num_processes):
    pid = i + 1
    priority = int(input(f"Enter priority for process {pid} (0-9): "))
    burst_time = int(input(f"Enter burst time for process {pid}: "))
    process = Process(pid, priority, burst_time)
    if priority in HIGH_PRIORITY_RANGE:
        high_priority_queue.append(process)
    elif priority in MEDIUM_PRIORITY_RANGE:
        medium_priority_queue.append(process)
    elif priority in LOW_PRIORITY_RANGE:
        low_priority_queue.append(process)

# Run the scheduling algorithm
quantum_time = 10
time_slice = 4

# Round Robin algorithm for highest priority queue
while high_priority_queue:
    current_process = high_priority_queue.pop(0)
    print(f"Running {current_process} from high priority queue for {quantum_time} seconds...")
    if current_process.remaining_time > time_slice:
        current_process.remaining_time -= time_slice
        high_priority_queue.append(current_process)
    else:
        current_process.remaining_time = 0

    # Switch to next queue after quantum time expires
    if quantum_time == 0:
        break
    quantum_time -= time_slice

# Priority Scheduling algorithm for medium priority queue
medium_priority_queue.sort(key=lambda p: p.priority)
for process in medium_priority_queue:
    print(f"Running {process} from medium priority queue for {process.burst_time} seconds...")

# First Come First Serve algorithm for lowest priority queue
for process in low_priority_queue:
    print(f"Running {process} from low priority queue for {process.burst_time} seconds...")
