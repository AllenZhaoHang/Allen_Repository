# Makefile for CS5600 PA1 - Unix Shell

CC = gcc
CFLAGS = -Wall -Werror -g
TARGET = shell
OUTPUT = output

all: $(TARGET) $(OUTPUT)

$(TARGET): shell.c
	$(CC) $(CFLAGS) -o $(TARGET) shell.c

$(OUTPUT): output.c
	$(CC) $(CFLAGS) -o $(OUTPUT) output.c

clean:
	rm -f $(TARGET) $(OUTPUT) *.o

.PHONY: all clean