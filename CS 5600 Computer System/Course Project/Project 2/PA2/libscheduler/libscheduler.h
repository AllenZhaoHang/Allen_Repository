/*
 * Programming Assignment 2
 * CS 5600, Spring 2026
 * Library for Scheduler Code
 * February 16, 2026
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum { FCFS, SJF, PSJF, PRI, PPRI, RR };
/*********************
FCFS = First-Come, First-Served
SJF  = Shortest Job First
PSJF = Premptive Shortest Job First
PRI  = Priority
PPRI = Premptive Priority
RR   = Round Robin
**********************/
extern int scheme;

void scheduler_show_queue();
int scheduler_new_job(int job_number, int time, int running_time, int priority);
int scheduler_job_finished(int job_number, int time);
int scheduler_quantum_expired(int time);
double scheduler_average_turnaround_time();
double scheduler_average_waiting_time();
double scheduler_average_response_time();
void scheduler_clean_up();
