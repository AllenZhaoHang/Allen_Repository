/**
 **  unix client access program
 **
 **/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "client.h"


#define default_server_number	233+1024


int main( int argc, char*argv[] )
{
char	*server_node;
int	server_number;

/*  there must be one or two command line arguments  */
if( argc > 3 || argc < 2 )
	{
	fprintf(stderr, "usage: client server-number [server-node]\n");
	exit(1);
	}

/*  get the server's port number from the first parameter  */
server_number = atoi(argv[1]);

/*  get the server's node name from the second parameter  */
if( argc <= 2 )
	server_node = NULL;
else
	server_node = argv[2];

/*  now let the common client do the real work  */
client( server_number, server_node );

return(0);
}


