# Build an executable using the following:
#
# clang barebones.s -o barebones  # clang is another compiler like gcc
#
.text
_barebones:

.data
	
.globl main

main:
				# (1) What are we setting up here?
				# Ans:
	pushq %rbp		# This instruction pushes the value of the base pointer (%rbp) onto the stack. 
	movq  %rsp, %rbp	# This instruction moves the current value of the stack pointer (%rsp) into the base pointer (%rbp). 

				# (2) What is going on here
				# Ans:
	movq $1, %rax		# This instruction moves the value 1 into the %rax register.
	movq $1, %rdi		# This instruction moves the value 1 into the %rdi register. 
	leaq .hello.str,%rsi	# This instruction loads the effective address (i.e., the memory address) of the string labeled .hello.str into the %rsi register. 

			# (3) What is syscall? We did not talk about this in class.
			# Ans: The syscall instruction is used to make a system call in x86_64 assembly language.

	syscall		# Which syscall is being run?
				# Ans: The syscall instruction here is used to invoke the system call specified by the values in the registers. In the previous instructions 									# the values were set up for the write system call. Therefore, the syscall here corresponds to the write system call.

				# (4) What would another option be instead of 
				# using a syscall to achieve this?
				# Ans: Another option to achieve printing to the standard output instead of using a syscall directly is to use a standard library function, 									# such as printf from the C library. The printf function is a higher-level function that abstracts away the details of system calls and 										# provides a more convenient interface for formatting and printing output

	movq	$60, %rax	# (5) We are again setting up another syscall
	movq	$0, %rdi	# What command is it?
				# Ans: the combination of these instructions is preparing the registers for the exit system call with an exit status of 0 syscall

	popq %rbp	# (Note we do not really need
			 	# this command here after the syscall)

.hello.str:
	.string "Hello World!\n"
	.size	.hello.str,13		# (6) Why is there a 13 here?
					# Ans:The .size directive is specifying the size of the string in bytes. In this case, it is indicating that the size of the string "Hello 											# World!\n" is 13 bytes.	
