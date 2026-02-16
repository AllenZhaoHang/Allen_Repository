#
# Programming Assignment 2
# CS 5600, Spring 2026
# Hang Zhao
# 2/16/2026
#

CC = gcc
INC = -I.
FLAGS = -W -g

all: simulator

simulator: simulator.o libscheduler/libscheduler.o
	$(CC) $^ -o $@

libscheduler/libscheduler.o: libscheduler/libscheduler.c libscheduler/libscheduler.h
	$(CC) -c $(FLAGS) $(INC) $< -o $@

simulator.o: simulator.c libscheduler/libscheduler.h
	$(CC) -c $(FLAGS) $(INC) $< -o $@

.PHONY : clean
clean:
	-rm -f simulator *.o libscheduler/*.o
