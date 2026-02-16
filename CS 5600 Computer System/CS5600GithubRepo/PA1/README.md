# CS5600 Programming Assignment 1: Unix Shell

## Student Information
- **Name**: Hang Zhao
- **NUID**: 002826538
- **GitHub Login**: https://github.khoury.northeastern.edu/biology000/CS5600_biology000

## Design Overview

This shell implementation is structured around a main processing loop that handles both interactive and batch modes. The program consists of several key components:

1. **Main Function**: Determines whether to run in interactive or batch mode based on command line arguments.

2. **Mode Handlers**:
   - `interactive_mode()`: Displays a prompt and reads commands from stdin
   - `batch_mode()`: Reads and executes commands from a batch file

3. **Command Processing Pipeline**:
   - `process_line()`: Orchestrates the execution of a complete line of input
   - `parse_commands()`: Splits input line by semicolons to extract individual commands
   - `parse_args()`: Tokenizes a command into executable arguments
   - `execute_command()`: Uses fork() and execvp() to run the command

4. **Key Design Decisions**:
   - Uses `fork()` to create child processes for each command
   - All commands on a line (separated by `;`) execute concurrently
   - Parent process waits for all children before accepting new input
   - Memory is managed carefully with `strdup()` and proper cleanup
   - Built-in `quit` command is handled specially without forking

## Complete Specification

### Handling Ambiguities

1. **Empty Commands Between Semicolons**:
   - Lines like `; cat file` or `cat file ;;; ls` are handled gracefully
   - Empty commands are detected during argument parsing and skipped
   - No error message is printed; execution continues with valid commands

2. **Extra Whitespace**:
   - Leading and trailing whitespace is stripped during tokenization
   - Multiple spaces between arguments are handled by `strtok_r()`

3. **Quit Command Behavior**:
   - If `quit` appears with other commands, all non-quit commands execute first
   - The shell waits for all processes to complete before exiting
   - Example: `cat file ; quit` will display the file contents before exiting

4. **Long Command Lines**:
   - Lines are limited to 512 characters (including newline)
   - The shell continues processing without crashing on long inputs
   - Truncation occurs naturally through `fgets()` buffer limit

5. **End of Input**:
   - Batch files without `quit` exit gracefully after last command
   - `Ctrl-D` in interactive mode is treated as EOF and exits cleanly

6. **Command Execution Errors**:
   - Non-existent commands print "Error: Command not found" to stderr
   - Shell continues accepting new commands after errors

## Implementation Details

### Concurrent Execution
Commands separated by semicolons are executed simultaneously using multiple child processes. The parent shell forks once for each command, stores all child PIDs, then waits for all children using `waitpid()`.

### Built-in Commands
The `quit` command is the only built-in command. It is detected before forking and causes the shell to exit after all other commands on the same line complete.

### Error Handling
- Invalid command line arguments: Print usage and exit
- Cannot open batch file: Print error and exit  
- Command not found: Print error to stderr and continue
- Fork failure: Print error and continue with remaining commands

## Known Bugs or Problems

No known bugs at this time. The shell has been tested with:
- Empty commands and multiple semicolons
- Extra whitespace in various positions
- Concurrent command execution
- Interactive and batch modes
- Error conditions (invalid files, non-existent commands)
- The provided `output.c` test program for concurrent execution

## Compilation and Usage

### Compile:
```bash
make
```

### Run in Interactive Mode:
```bash
./shell
```

### Run in Batch Mode:
```bash
./shell batchfile.txt
```

### Clean Build Files:
```bash
make clean
```

## Testing

The shell has been tested with various scenarios including:
- Single commands: `ls`, `/bin/ls -l`
- Multiple concurrent commands: `ls ; pwd ; date`
- Commands with quit: `cat file ; quit`
- Empty and malformed inputs
- The provided `output` test program for concurrent execution verification