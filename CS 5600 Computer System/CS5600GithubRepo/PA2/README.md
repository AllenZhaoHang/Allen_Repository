# CS 5600 Programming Assignment 2: Process Scheduler
# name: Hang Zhao
# date: 2/16/2026

## Overview
This project implements a process scheduler library (`libscheduler`) that interacts with a discrete event simulator. The scheduler supports six different scheduling algorithms:
1. First-Come, First-Served (FCFS)
2. Shortest Job First (SJF)
3. Preemptive Shortest Job First (PSJF)
4. Priority (PRI)
5. Preemptive Priority (PPRI)
6. Round Robin (RR)

## Implementation Details
The scheduler uses a **linked list** to manage the queue of jobs. 

- **Job Struct**: defined as `job_t`, containing job ID, priority, arrival time, running time, remaining time, start time, etc.
- **Queue**: A singly linked list where `head` points to the first job.
- **Job Selection**:
    - **FCFS**: Selects the job with the earliest arrival time.
    - **SJF/PSJF**: Selects the job with the shortest running/remaining time.
    - **PRI/PPRI**: Selects the job with the highest priority (lowest integer value).
    - **RR**: Selects the head of the queue. On quantum expiration, the current job is moved to the tail.
- **Metrics**: 
    - **Waiting Time**: Total time spent in the ready queue.
    - **Turnaround Time**: Total time from arrival to completion.
    - **Response Time**: Time from arrival to the *first* time the job is scheduled.

## Compilation and Running
To compile the project, run:
```bash
make
```
This will produce the `simulator` executable.

To run the simulator with a specific scheme and input file:
```bash
./simulator <scheme> <input_file>
```
Examples:
```bash
./simulator fcfs examples/proc1.csv
./simulator rr2 examples/proc2.csv
```

## Verification
A verification script `verify_all.sh` is provided to run all test cases against the example outputs.
```bash
bash verify_all.sh
```
All provided test cases pass.
