# Homework 2 

This is the starting readme for this assignment.  Please edit the following 
information by removing the "*edit me*" and replace it with appropriate 
information your assignment. If it is asking you a question, please provide 
a response.

- Name: Hang Zhao
- Title: Homework — Module 2
- How many hours did it take you to complete this assignment? 3 hours
- Did you collaborate with any other students/TAs/Professors? If so, tell us 
  who and in what capacity.
  - Ziyue Shen, Peizhi Yan
- Did you use any external resources? (Cite them below)
  - CSDN, Google, Stackoverflow
  - https://gcc.gnu.org/onlinedocs/cpp/Header-Files.html
- (Optional) What was your favorite part of the assignment? 
  - *edit me*
- (Optional) How would you improve the assignment? 
  - *edit me*

## Logistics

For this assignment (and every assignment/lab), you must login into the 
servers through `your_khoury_name@login.khoury.northeastern.edu` to complete 
and test your work. The reason is the examples I will provide below are 
compiled strictly for our machine's architecture, and this is a consistent 
architecture where your submission will be graded.

### Important notes

* Your code **must compile and run** on the Khoury machines to earn credit. 
  Make sure you test your programs on these machines, as this is where we 
  grade your assignments.
* You must commit any additional files (if any) into your repository so we 
  can test your code.
  * Points will be lost if you forget!
* Do not forget to push your changes to your repo before the assignment 
  deadline!**

*****************************************************************
1.Why is a ring buffer useful and/or when should it be used? 

Answer:
Ring buffers, also referred to as circular queues, are useful in high-performance and operating systems because they provide a number of benefits. They have the important benefit of efficient memory consumption. A ring buffer uses a fixed-size buffer with a wrap-around feature, in contrast to linear data structures. This makes it especially effective in situations where memory management is crucial since it enables continuous data storage without the requirement for dynamic memory allocation or frequent resizing. Memory resources are not wasted because of the circular structure, which makes it possible to reuse memory regions.

The constant-time complexity of the enqueue and dequeue procedures is another important feature.  The time required to add or remove an element from the ring buffer is constant, independent of the buffer's size.  This is important in situations like audio processing, embedded systems, and real-time systems where reliable and quick data processing is needed.  For instance, a ring buffer can be used in audio applications to effectively store and process incoming audio samples, guaranteeing a timely and consistent output.

Ring buffers provide benefits, but they can have drawbacks.  The fixed size is one prominent restriction, which might be problematic if there are more elements to be saved than the buffer can hold.  Careful thought is required in these situations to prevent data loss or performance impairment.  Ultimately, the choice to employ a ring buffer is based on the particular needs of the system, where constant-time operations and effective memory utilization surpass the constraints of a fixed-size structure.

2. Why is a stack useful and/or when should it be used?

Answer:
Stacks are essential data structures that can be used in a wide range of computer settings due to their versatility.  Stacks are valuable primarily because they are Last In, First Out (LIFO) systems.  This indicates that the first element to be deleted from the stack is the one that was inserted last.  This feature is useful for handling nested structures or in situations where data must be processed in reverse order.  For instance, a stack can be used to evaluate and execute operands and operators in the opposite order that they appear in parsed expressions.

The extensive use of stack operations can be attributed to their efficiency and simplicity.  Stacks are effective for organizing and controlling elements because the push and pop operations—which involve adding and deleting elements from the stack, respectively—have a constant time complexity.  Programming languages' function call handling is one area where stacks are especially helpful.  A function's execution context is pushed onto the call stack when it is called, and it is removed after the function is finished.  By ensuring correct execution flow, this method makes it possible to manage function calls and returns in an organized manner.

Stacks have benefits, but they can have drawbacks.  A stack's fixed-size design may cause overflow if there are more items than the space allotted.  Moreover, stacks don't allow for random access to elements, which could be a limitation in some situations.  However, stacks are useful tools in programming and system design because of their ease of use, effectiveness, and well-defined behavior—particularly when handling nested structures or function calls.