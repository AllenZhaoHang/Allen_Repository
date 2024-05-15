/**
 ** client.c  -  a server program that uses the socket interface to tcp 
 **
 **/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>
#include <netinet/in.h>
#include "client.h"

extern char *inet_ntoa( struct in_addr );

#define NAMESIZE		255
#define BUFSIZE			81

void client( int server_number, char *server_node )
{
int			length;
int			n, len;
short			fd;
struct sockaddr_in	address;
struct hostent		*node_ptr;
char			local_node[NAMESIZE];
char			buffer[BUFSIZE];

/*  get the internet name of the local host node on which we are running  */
if( gethostname( local_node, NAMESIZE ) < 0 )
	{
	perror( "client gethostname" );
	exit(1);
	}
fprintf(stderr, "client running on node %s\n", local_node);

/*  get the name of the remote host node on which we hope to find server  */
if( server_node == NULL )
	server_node = local_node;
fprintf(stderr, "client about to connect to server at port number %d on node %s\n",
		server_number, server_node);

/*  get structure for remote host node on which server resides  */
if( (node_ptr = gethostbyname( server_node )) == NULL )
	{
	perror( "client gethostbyname" );
	exit(1);
	}

/*  set up Internet address structure for the server  */
memset(&address, 0, sizeof(address));
address.sin_family = AF_INET;
memcpy(&address.sin_addr, node_ptr->h_addr, node_ptr->h_length);
address.sin_port = htons(server_number);

fprintf(stderr, "client full name of server node %s, internet address %s\n",
		node_ptr->h_name, inet_ntoa(address.sin_addr));

/*  open an Internet tcp socket  */
if( (fd = socket(AF_INET, SOCK_STREAM, 0)) < 0 )
	{
	perror( "client socket" );
	exit(1);
	}

/*  connect this socket to the server's Internet address  */
if( connect( fd, (struct sockaddr *)&address, sizeof(address) ) < 0 )
	{
	perror( "client connect" );
	exit(1);
	}

/*  now find out what local port number was assigned to this client  */
len = sizeof(address);
if( getsockname( fd, (struct sockaddr *)&address, &length ) < 0 )
	{
	perror( "client getsockname" );
	exit(1);
	}

/*  we are now successfully connected to a remote server  */
fprintf(stderr, "client at internet address %s, port %d\n",
		inet_ntoa(address.sin_addr), ntohs(address.sin_port));

/*  transmit data from standard input to server  */
while( fgets( buffer, BUFSIZE, stdin ) != NULL )
	{
	len = strlen(buffer);
	if( (n = send(fd, buffer, len, 0)) != len )
		if( n < 0 )
			{
			perror( "client send" );
			exit(1);
			}
		else
			{
			fprintf(stderr, "client sent %d bytes, attempted %d\n", n, len);
			break;
			}
	}

/*  close the connection to the server  */
if( close(fd) < 0 )
	{
	perror( "client close" );
	exit(1);
	}
}
