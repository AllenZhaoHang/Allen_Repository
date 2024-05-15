#
#
#  Makefile for client and server examples
#
#

# Edit the following line to reflect the current project number
PROJNUM = 1

HDR = client.h server.h
SRC = client.c server.c unixclient.c unixserver.c

OBJ = unixclient.o unixserver.o server.o client.o
GRD = makefile ${SRC} ${HDR}

CC=gcc
CFLAGS = -g0

# Create all files

all:	client server

client:	unixclient.o client.o
	$(CC)	$(CFLAGS) unixclient.o client.o -o client

server:	unixserver.o server.o
	$(CC)	$(CFLAGS) unixserver.o server.o -o server

unixclient.o:	unixclient.c client.h
	$(CC)	$(CFLAGS) -c unixclient.c
	
client.o:	client.c client.h
	$(CC)	$(CFLAGS) -c client.c

unixserver.o:	unixserver.c server.h
	$(CC)	$(CFLAGS) -c unixserver.c

server.o:	server.c server.h
	$(CC)	$(CFLAGS) -c server.c

#
# Clean up script
#
clean:
	/bin/rm -f *.o client server

