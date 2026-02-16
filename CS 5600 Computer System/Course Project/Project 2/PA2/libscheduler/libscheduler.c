/**
 * Programming Assignment 2
 * CS 5600, Spring 2026
 * Library for Scheduler Code
 * February 16, 2026
 */

#include "libscheduler.h"

int scheme = -1; // If this fails, try NULL here instead of -1

/*
 * You may need to define some global variables or a struct to
 * store your job queue elements. Feel free to do it here at the
 * top of the .c file, or in the .h file.
 */

typedef struct job {
  int job_number;
  int arrival_time;
  int running_time;
  int priority;
  int remaining_time;
  int start_time; // Time first scheduled
  int finish_time;
  int last_scheduled_time; // Time when it was last picked to run
} job_t;

typedef struct node {
  job_t *job;
  struct node *next;
} node_t;

node_t *head = NULL;
job_t *current_job = NULL;

// Statistics
double total_waiting_time = 0.0;
double total_turnaround_time = 0.0;
double total_response_time = 0.0;
int completed_jobs_count = 0;

// Helper to add a job to the end of the list
void add_job(job_t *new_job) {
  node_t *new_node = (node_t *)malloc(sizeof(node_t));
  new_node->job = new_job;
  new_node->next = NULL;

  if (head == NULL) {
    head = new_node;
  } else {
    node_t *current = head;
    while (current->next != NULL) {
      current = current->next;
    }
    current->next = new_node;
  }
}

// Helper to remove a job from the list
void remove_job(int job_number) {
  if (head == NULL)
    return;

  node_t *temp = head;
  node_t *prev = NULL;

  // If head holds the key
  if (temp != NULL && temp->job->job_number == job_number) {
    head = temp->next;
    free(temp); // Free node only, job is freed elsewhere or handled
    return;
  }

  // Search for the key
  while (temp != NULL && temp->job->job_number != job_number) {
    prev = temp;
    temp = temp->next;
  }

  // If key was not present
  if (temp == NULL)
    return;

  // Unlink the node from linked list
  prev->next = temp->next;
  free(temp);
}

// Comparison function for sorting/selecting jobs based on scheme
// Returns > 0 if job A is "worse" than job B (B should run)
// Returns < 0 if job A is "better" than job B (A should run)
// Returns 0 if equal (tie-breaker needed)
int compare_jobs(job_t *a, job_t *b) {
  if (a == NULL)
    return 1;
  if (b == NULL)
    return -1;

  if (scheme == FCFS) {
    return a->arrival_time - b->arrival_time;
  } else if (scheme == SJF) {
    if (a->running_time != b->running_time)
      return a->running_time - b->running_time;
    return a->arrival_time - b->arrival_time;
  } else if (scheme == PSJF) {
    if (a->remaining_time != b->remaining_time)
      return a->remaining_time - b->remaining_time;
    return a->arrival_time - b->arrival_time;
  } else if (scheme == PRI || scheme == PPRI) {
    if (a->priority != b->priority)
      return a->priority - b->priority;
    return a->arrival_time - b->arrival_time;
  } else if (scheme == RR) {
    // RR logic is handled by queue order, so this might not be used directly
    // for selection But if we just pick the head, it's fine.
    return 0;
  }
  return 0;
}

// Select the next job to run
job_t *find_next_job(int time) {
  if (head == NULL)
    return NULL;

  if (scheme == RR) {
    return head->job;
  }

  node_t *current = head;
  job_t *best_job = current->job;

  while (current != NULL) {
    if (compare_jobs(current->job, best_job) < 0) {
      best_job = current->job;
    }
    current = current->next;
  }
  return best_job;
}

/* See Canvas function descriptions for details of each function */

void scheduler_show_queue() {
  node_t *current = head;
  while (current != NULL) {
    printf("%d ", current->job->job_number);
    current = current->next;
  }
}

int scheduler_new_job(int job_number, int time, int running_time,
                      int priority) {
  job_t *new_job = (job_t *)malloc(sizeof(job_t));
  new_job->job_number = job_number;
  new_job->arrival_time = time;
  new_job->running_time = running_time;
  new_job->priority = priority;
  new_job->remaining_time = running_time;
  new_job->start_time = -1;
  new_job->last_scheduled_time = -1;

  add_job(new_job);

  // If no job is currently running, schedule the best one
  if (current_job == NULL) {
    current_job = find_next_job(time);
    if (current_job) {
      // If it's starting for the first time
      if (current_job->start_time == -1) {
        current_job->start_time = time;
      }
      current_job->last_scheduled_time = time;
    }
    return current_job ? current_job->job_number : -1;
  }

  // Preemptive check
  if (scheme == PSJF || scheme == PPRI) {
    // Update remaining time of current job before comparing?
    // Simulator calls new_job at the start of a unit.
    // If current_job was running, we should update its remaining time?
    // Wait, logic: simulator calls new_job.
    // If we switch, the switch happens "now".
    // The previous job ran up until "now".
    // We need to account for the time passed since last decision?
    // Actually, simulator updates time_left in its own structure.
    // But we need to update our `remaining_time`.
    // `scheduler_new_job` is called. `time` is current time.
    // `current_job->last_scheduled_time` holds when it started this
    // quantum/block.

    int time_ran = time - current_job->last_scheduled_time;
    current_job->remaining_time -= time_ran;
    current_job->last_scheduled_time = time;

    job_t *best = find_next_job(time);
    if (best != current_job) {
      // If the current job just started (start_time == time) and ran for 0
      // time, it means it was picked in job_finished() but immediately
      // preempted by this new job before running. So we should reset its
      // start_time.
      if (time_ran == 0 && current_job->start_time == time) {
        current_job->start_time = -1;
      }

      // Context switch
      current_job = best;
      if (current_job->start_time == -1) {
        current_job->start_time = time;
      }
      current_job->last_scheduled_time = time;
    }
    return current_job->job_number;
  }

  // Non-preemptive schemes (FCFS, SJF, PRI) - continue current job
  if (scheme != RR)
    return current_job->job_number;

  // RR: new job logic. "In RR, when a new job arrives, it must be placed at the
  // end of the cycle of jobs." We already added it to end of list. Should we
  // switch? Only if current job finished or quantum expired. But new_job is
  // just "adding to queue". If current_job is running, it continues until
  // quantum expires.
  return current_job->job_number;
}

int scheduler_job_finished(int job_number, int time) {
  // Current job finished. Update metrics.
  // Note: job_number might be different from current_job->job_number if
  // something went wrong, but we assume it matches `current_job` in normal
  // operation. Or rather, we should find the job in our list that matches
  // `job_number`. But `current_job` should be it.

  if (current_job == NULL || current_job->job_number != job_number) {
    // Should not happen based on simulator behavior?
    // Actually, let's find the job to be safe, or just assume current_job.
    // But better: use the job_number to find it in the list (if we kept it
    // there).
  }

  // Calculate stats
  // Waiting time = (Finish - Arrival) - Running
  // Turnaround = Finish - Arrival
  // Response = Start - Arrival

  total_turnaround_time += (time - current_job->arrival_time);
  total_waiting_time +=
      (time - current_job->arrival_time) - current_job->running_time;
  total_response_time += (current_job->start_time - current_job->arrival_time);
  completed_jobs_count++;

  remove_job(job_number);
  free(current_job); // Free the memory for the job struct
  current_job = NULL;

  // Pick next job
  current_job = find_next_job(time);
  if (current_job != NULL) {
    if (current_job->start_time == -1) {
      current_job->start_time = time;
    }
    current_job->last_scheduled_time = time;
    return current_job->job_number;
  }

  return -1;
}

int scheduler_quantum_expired(int time) {
  if (scheme != RR) {
    // Should not happen
    return -1;
  }

  // Update current job's remaining time (though for RR selection it doesn't
  // matter, but for tracking yes)
  if (current_job) {
    int time_ran = time - current_job->last_scheduled_time;
    current_job->remaining_time -= time_ran;
    current_job->last_scheduled_time = time;

    // Move current job to end of list
    // 1. Remove from head (it should be at head for RR)
    // 2. Add to tail
    // Actually, our `add_job` adds to tail.
    // So detailed logic:
    node_t *old_head = head;
    if (head->next != NULL) { // Only rotate if > 1 job
      head = head->next;
      old_head->next = NULL;

      node_t *curr = head;
      while (curr->next != NULL)
        curr = curr->next;
      curr->next = old_head;
    }
  }

  // Pick new head
  current_job = find_next_job(time); // Will pick head
  if (current_job) {
    if (current_job->start_time == -1) {
      current_job->start_time = time;
    }
    current_job->last_scheduled_time = time;
    return current_job->job_number;
  }

  return -1;
}

double scheduler_average_waiting_time() {
  if (completed_jobs_count == 0)
    return 0.0;
  return total_waiting_time / completed_jobs_count;
}

double scheduler_average_turnaround_time() {
  if (completed_jobs_count == 0)
    return 0.0;
  return total_turnaround_time / completed_jobs_count;
}

double scheduler_average_response_time() {
  if (completed_jobs_count == 0)
    return 0.0;
  return total_response_time / completed_jobs_count;
}

void scheduler_clean_up() {
  // Free any remaining nodes/jobs
  while (head != NULL) {
    node_t *temp = head;
    head = head->next;
    free(temp->job);
    free(temp);
  }
}
