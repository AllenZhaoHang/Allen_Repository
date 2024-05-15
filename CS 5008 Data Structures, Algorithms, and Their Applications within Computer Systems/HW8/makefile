####################
# Makefile for Traveling Map
####################

CC=gcc
CFLAGS=-Wall -g

map: main.o
	$(CC) $(CFLAGS) -o map main.o

main.o: main.c my_dll.h my_graph.h
	$(CC) $(CFLAGS) -c main.c

clean:
	rm map
	rm *.o
