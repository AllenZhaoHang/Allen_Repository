/**
 ** server.c  -  a server program that uses the socket interface to tcp 
 **
 **/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>
#include <netinet/in.h>
#include "server.h"

extern char *inet_ntoa( struct in_addr );

#define NAMESIZE		255
#define BUFSIZE			81
#define listening_depth		2

void server( int server_number )
{
int			c, i, q;
int			n, len;
short			fd, client_fd;
struct sockaddr_in	address, client;
struct hostent		*node_ptr;
char			local_node[NAMESIZE];
char			buffer[BUFSIZE+1];
char			buffer2[BUFSIZE+1];

/*  get the internet name of the local host node on which we are running  */
if( gethostname( local_node, NAMESIZE ) < 0 )
	{
	perror( "server gethostname" );
	exit(1);
	}
fprintf(stderr, "server running on node %s\n", local_node);

/*  get structure for local host node on which server resides  */
if( (node_ptr = gethostbyname( local_node )) == NULL )
	{
	perror( "server gethostbyname" );
	exit(1);
	}

/*  set up Internet address structure for the server  */
memset(&address, 0, sizeof(address));
address.sin_family = AF_INET;
memcpy(&address.sin_addr, node_ptr->h_addr, node_ptr->h_length);
address.sin_port = htons(server_number);

fprintf(stderr, "server full name of server node %s, internet address %s\n",
		node_ptr->h_name, inet_ntoa(address.sin_addr));

/*  open an Internet tcp socket  */
if( (fd = socket(AF_INET, SOCK_STREAM, 0)) < 0 )
	{
	perror( "server socket" );
	exit(1);
	}

/*  bind this socket to the server's Internet address  */
if( bind( fd, (struct sockaddr *)&address, sizeof(address) ) < 0 )
	{
	perror( "server bind" );
	exit(1);
	}

/*  now find out what local port number was assigned to this server  */
len = sizeof(address);
if( getsockname( fd, (struct sockaddr *)&address, &len ) < 0 )
	{
	perror( "server getsockname" );
	exit(1);
	}

/*  we are now successfully established as a server  */
fprintf(stderr, "server at internet address %s, port %d\n",
		inet_ntoa(address.sin_addr), ntohs(address.sin_port));

/*  start listening for connect requests from clients  */
if( listen( fd, listening_depth ) < 0 )
	{
	perror( "server listen" );
	exit(1);
	}

/*  now accept a client connection (we'll block until one arrives)  */
len = sizeof(client);
if( (client_fd = accept(fd, (struct sockaddr *)&client, &len)) < 0 )
	{
	perror( "server accept" );
	exit(1);
	}

/*  we are now successfully connected to a remote client  */
fprintf(stderr, "server connected to client at Internet address %s, port %d\n",
		inet_ntoa(client.sin_addr), ntohs(client.sin_port));

/* This part displays the text sent from the client */
while( (n = recv( client_fd, buffer, BUFSIZE, 0)) > 0 )
	{
	buffer[n] = '\0';
	n--;
	if( buffer[n] == '\n' )
		n--;
	//
	for(q=0; q<=n; q++) {
		buffer2[q]=buffer[n-q];
		//printf("buffer[%d]: %c\n",q,buffer[q]);
		//printf("buffer2[%d]: %c\n",n-q,buffer[n-q]);
	}
	buffer2[n+1]='\n';
	buffer2[n+2]='\0';
	fputs(buffer2, stdout);
	//fputs(buffer, stdout);
	}
/* End of the work that is done to display the text from the client */

if( n < 0 )
	perror( "server read" );

/*  close the connection to the client  */
if( close(client_fd) < 0 )
	{
	perror( "server close connection to client" );
	exit(1);
	}

/*  close the "listening post" socket by which server made connections  */
if( close(fd) < 0 )
	{
	perror( "server close" );
	exit(1);
	}
}

