#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#define MAX_LINE_LENGTH 512
#define MAX_ARGS 64
#define MAX_COMMANDS 32
/* Name : Hang Zhao
   Date : 01-25-2025
*/
/* Function prototypes */
void interactive_mode();
void batch_mode(char *filename);
void process_line(char *line);
int parse_commands(char *line, char *commands[]);
int parse_args(char *command, char *args[]);
void execute_command(char *args[]);
int is_quit_command(char *command);
void print_error(char *message);

int main(int argc, char *argv[]) {
    /* Check command line arguments */
    if (argc > 2) {
        print_error("Usage: shell [batchFile]\n");
        exit(1);
    }

    if (argc == 2) {
        /* Batch mode */
        batch_mode(argv[1]);
    } else {
        /* Interactive mode */
        interactive_mode();
    }

    return 0;
}

/* Interactive mode: display prompt and read from stdin */
void interactive_mode() {
    char line[MAX_LINE_LENGTH];
    
    while (1) {
        printf("prompt> ");
        fflush(stdout);
        
        if (fgets(line, MAX_LINE_LENGTH, stdin) == NULL) {
            /* Ctrl-D pressed or EOF */
            break;
        }
        
        /* Remove newline character */
        line[strcspn(line, "\n")] = 0;
        
        process_line(line);
    }
}

/* Batch mode: read commands from file */
void batch_mode(char *filename) {
    FILE *fp = fopen(filename, "r");
    char line[MAX_LINE_LENGTH];
    
    if (fp == NULL) {
        print_error("Error: Cannot open batch file\n");
        exit(1);
    }
    
    while (fgets(line, MAX_LINE_LENGTH, fp) != NULL) {
        /* Remove newline character */
        line[strcspn(line, "\n")] = 0;
        
        /* Echo the command */
        printf("%s\n", line);
        fflush(stdout);
        
        process_line(line);
    }
    
    fclose(fp);
}

/* Process a single line of input */
void process_line(char *line) {
    char *commands[MAX_COMMANDS];
    int num_commands;
    int i;
    pid_t pids[MAX_COMMANDS];
    int num_processes = 0;
    int has_quit = 0;
    
    /* Parse commands separated by ; */
    num_commands = parse_commands(line, commands);
    
    /* Check if any command is quit */
    for (i = 0; i < num_commands; i++) {
        if (is_quit_command(commands[i])) {
            has_quit = 1;
            break;
        }
    }
    
    /* Execute all non-quit commands concurrently */
    for (i = 0; i < num_commands; i++) {
        if (is_quit_command(commands[i])) {
            continue;
        }
        
        char *args[MAX_ARGS];
        int num_args = parse_args(commands[i], args);
        
        /* Skip empty commands */
        if (num_args == 0) {
            continue;
        }
        
        /* Fork and execute */
        pid_t pid = fork();
        
        if (pid < 0) {
            print_error("Error: Fork failed\n");
            continue;
        } else if (pid == 0) {
            /* Child process */
            execute_command(args);
            /* If execvp returns, there was an error */
            print_error("Error: Command not found\n");
            exit(1);
        } else {
            /* Parent process */
            pids[num_processes++] = pid;
        }
    }
    
    /* Wait for all child processes to complete */
    for (i = 0; i < num_processes; i++) {
        waitpid(pids[i], NULL, 0);
    }
    
    /* Exit if quit was found */
    if (has_quit) {
        exit(0);
    }
}

/* Parse commands separated by ; */
int parse_commands(char *line, char *commands[]) {
    int count = 0;
    char *line_copy = strdup(line);
    char *token;
    char *saveptr;
    
    token = strtok_r(line_copy, ";", &saveptr);
    
    while (token != NULL && count < MAX_COMMANDS) {
        commands[count++] = strdup(token);
        token = strtok_r(NULL, ";", &saveptr);
    }
    
    free(line_copy);
    return count;
}

/* Parse arguments within a command */
int parse_args(char *command, char *args[]) {
    int count = 0;
    char *command_copy = strdup(command);
    char *token;
    char *saveptr;
    
    /* Tokenize by whitespace */
    token = strtok_r(command_copy, " \t\n", &saveptr);
    
    while (token != NULL && count < MAX_ARGS - 1) {
        args[count++] = strdup(token);
        token = strtok_r(NULL, " \t\n", &saveptr);
    }
    
    args[count] = NULL;  /* NULL terminate the array */
    free(command_copy);
    
    return count;
}

/* Execute a command using execvp */
void execute_command(char *args[]) {
    if (args[0] == NULL) {
        exit(0);
    }
    
    execvp(args[0], args);
    /* If execvp returns, there was an error */
}

/* Check if command is quit */
int is_quit_command(char *command) {
    char *args[MAX_ARGS];
    int num_args = parse_args(command, args);
    int result = 0;
    
    if (num_args > 0 && strcmp(args[0], "quit") == 0) {
        result = 1;
    }
    
    /* Free allocated memory */
    int i;
    for (i = 0; i < num_args; i++) {
        free(args[i]);
    }
    
    return result;
}

/* Print error message to stderr */
void print_error(char *message) {
    fprintf(stderr, "%s", message);
}