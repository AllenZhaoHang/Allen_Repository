/*
 * Programming Assignment 2
 * CS 5600, Spring 2026
 * Simulator Code
 * February 3, 2026
 */


/*
NOTE:
It is not important to understand what this code does. This code will call 
the functions defined in scheduler.c and, based on the return values of 
those functions, will schedule the specific job in the discrete event simulator.

You should not modify this code. You should also not make use of any variables
in this file (don't use the "__simulator_internal_structure__job" struct, 
make your own; you'll find that this data structure doesn't contain all the 
fields you will need).
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "libscheduler/libscheduler.h"


struct __simulator_internal_structure__job
{
	int time_left;
	int arrival_time;
	short int active;
	int priority;
};

struct __simulator_internal_structure__job __simulator_internal_structure__jobs[100];
char __simulator_internal_structure__timing_diagram[256];

int main(int argc, char **argv) {
	FILE *fp;
	int i=0, rr=0, quantum=0, next_quantum=0, next_job=0, current_job=0, total_jobs=0, current_time=0;
	char scheme_name[5], s1[16];
	if(argc<3){
		fprintf(stderr,"Usage: %s <scheme> <jobs file>\n",argv[0]);
		exit(-1);
	}

	strncpy(scheme_name, argv[1],4);
	scheme_name[4]='\0';
	if(!strncmp(scheme_name,"rr",2)){
		rr=1;
		scheme = RR;
		quantum = atoi(scheme_name+2);
		if (quantum <=0){
			fprintf(stderr, "Invalid time quantum for Round-Robin Process Scheduling Algorithm.\n");
			exit(-4);
		}
	}	 
	else{
		rr=0;
		quantum = 0;
		/* FIguring out the scheduling algorithm to be used*/
		if (!strcmp(scheme_name,"fcfs"))
			scheme = FCFS;
		else if (!strcmp(scheme_name,"sjf"))
			scheme = SJF;
		else if (!strcmp(scheme_name,"psjf"))
			scheme = PSJF;
		else if (!strcmp(scheme_name,"pri"))
			scheme = PRI;
		else if (!strcmp(scheme_name,"ppri"))
			scheme = PPRI;
		else {
			fprintf(stderr,"Invalid scheduling algorithm.\n");
			fprintf(stderr,"Acceptable algorithms are:\n");
			fprintf(stderr,"\tfcfs, sjf, psjf, pri, ppri, rr#\n");
			exit(-6);
		}
	}	

	// Collect process data in advance, store in __simulator_internal_structure__jobs[]
	fp = fopen(argv[2],"r");
	if (fp == NULL) {
		perror("Can't open input file");
		exit(-2);
	}
	i=0;

	if (fscanf(fp,"\"%15[^,\"]\",\"%15[^,\"]\",\"%15[^,\"]\"\n",s1,s1,s1) != 3) {
		fprintf(stderr,"Invalid input file format.\n");
		exit(-5);
	}

	while(fscanf(fp,"%d,%d,%d\n",&(__simulator_internal_structure__jobs[i].arrival_time),&(__simulator_internal_structure__jobs[i].time_left),&(__simulator_internal_structure__jobs[i].priority))>0) {
		__simulator_internal_structure__jobs[i].active = 0;
		i++;
	}

	printf("Loaded %d jobs.\n\n\n",i);
	// initialize
	total_jobs = i;
	next_job = 0;
	current_job = -1;
	current_time = 0;

	// loop as long as there is a current job, or more jobs to process later
	while(current_job >=0 || next_job < total_jobs) { 

		/* For every cycle (when appropriate):
		 * 1) Update quantum
		 * 2) Update timing diagram
		 * 3) Update job status
		 * 4) Call scheduler
		 * 5) Update clock
		*/

		int next_start=0, next_finish=0, prev_finish=-1;
	
		// Show status
		printf("Current time: %d\t Current job %d\n",current_time, current_job);
		printf("Timing diagram: %s\n",__simulator_internal_structure__timing_diagram);
		printf("Process queue: ");
		scheduler_show_queue();
		printf("\n\n");
	
		if (current_job == -1) {       // if current_job == -1 then the queue is empty
			if (next_job >= total_jobs)
				break;                    // no more jobs: quit

			else {                      // wait for new job
				next_start = __simulator_internal_structure__jobs[next_job].arrival_time;
				__simulator_internal_structure__jobs[next_job].active = 1;
				if (rr)
					next_quantum = ((int)(current_time/quantum+1))*quantum;
				for(i=current_time;i<next_start;i++)
					__simulator_internal_structure__timing_diagram[i]='-';
				printf("New job %d at time %d.\n", next_job, next_start);
				current_job = scheduler_new_job(next_job, next_start, 
				__simulator_internal_structure__jobs[next_job].time_left, 
				__simulator_internal_structure__jobs[next_job].priority);
				current_time = next_start;
				next_job++;
			}
			continue;
		}

		// Only valid jobs should be processed
		if(!__simulator_internal_structure__jobs[current_job].active) {
			fprintf(stderr, "Scheduler selected invalid job.\n");
			exit(-3);
		}

		/* There are 3 possible events: 
		   -a new job, 
		   -a job finishes, and
		   -the quantum expires. 
		   Check all three and take the earliest one, as long as it is valid.
		   In case of a tie, a finished job takes prioirty over a new quantum, 
		   which takes priority over a new job.
		*/

		while (rr && next_quantum < current_time)
			next_quantum += quantum;

		next_start = __simulator_internal_structure__jobs[next_job].arrival_time;
		next_finish = current_time + __simulator_internal_structure__jobs[current_job].time_left;

		if(rr && (next_quantum <= next_start || next_job >= total_jobs) && next_quantum < next_finish) {
			for(i=current_time;i<next_quantum;i++)
				__simulator_internal_structure__timing_diagram[i] = current_job + '0';
			__simulator_internal_structure__jobs[current_job].time_left -= (next_quantum - current_time);
			printf("Tick at time %d.\n",next_quantum);
			if(current_time > prev_finish)
        current_job = scheduler_quantum_expired(next_quantum);
			current_time = next_quantum;
			next_quantum += quantum;
		}
		else if (next_start < next_finish && next_job < total_jobs) {
			for(i=current_time;i<next_start;i++)
				__simulator_internal_structure__timing_diagram[i] = current_job + '0';
			__simulator_internal_structure__jobs[current_job].time_left -= (next_start - current_time);
			__simulator_internal_structure__jobs[next_job].active = 1;
			printf("New job %d at time %d.\n", next_job, next_start);
			current_job = scheduler_new_job(next_job, next_start, __simulator_internal_structure__jobs[next_job].time_left, __simulator_internal_structure__jobs[next_job].priority);
			current_time = next_start;
			next_job++;
		} 
		else {
			for(i=current_time;i<next_finish;i++)
				__simulator_internal_structure__timing_diagram[i] = current_job + '0';
			__simulator_internal_structure__jobs[current_job].time_left -= (next_finish - current_time);
			__simulator_internal_structure__jobs[current_job].active = 0;
			printf("Job %d finished at time %d.\n", current_job, next_finish);
			current_job = scheduler_job_finished(current_job, next_finish);
			current_time = next_finish;
			prev_finish = next_finish;
			next_quantum = current_time + quantum;
		}
	}

	__simulator_internal_structure__timing_diagram[current_time]='\0';
	printf("\n\nFinal timing diagram:\n\t%s\n",__simulator_internal_structure__timing_diagram);
	printf("Average Response Time: %1.2f\n", scheduler_average_response_time());
	printf("Average Waiting Time: %1.2f\n", scheduler_average_waiting_time());
	printf("Average Turnaround Time: %1.2f\n", scheduler_average_turnaround_time());

	fclose(fp);
	scheduler_clean_up();
	return 0;
}

