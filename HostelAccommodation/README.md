# hostelAccommodation-withFileHandling

Overview:
The Hostel Accommodation System is a C++ application designed to manage hostel room reservations and track student details. The system allows students to reserve beds, checks for availability, and stores information about the hostel and students in text files. The program provides a command-line interface (CLI) to interact with the system, reserve a bed, or exit the application.

Features:
Hostel Bed Reservation: Allows users to reserve a bed if available. Updates the bed count dynamically and ensures no overbooking.
Student Registration: Collects and stores student details, including name, roll number, and address, into a text file.
File-based Storage: Stores hostel and student data in Hostel.txt and Student.txt files, ensuring persistence between system runs.
User Interaction: Provides a user-friendly CLI for easy operation and navigation. Users can choose to reserve a bed or exit the system.
Bed Availability Check: Displays an error message when no beds are available for reservation.
Technologies Used:
C++: Core programming language used for implementing the system.
File Handling: ifstream and ofstream for reading and writing to text files.
String Manipulation: Utilizes find(), replace(), and stringstream to update and manage text-based data.
Windows API: Sleep function used to pause between operations for improved user experience.
Object-Oriented Programming (OOP): Classes for Hostel and Student entities to manage data and behavior.
Command-Line Interface (CLI): User interface for interacting with the system.
Instructions:
Compile the program using a C++ compiler.
Run the executable.
Follow the on-screen instructions to reserve a bed or exit the program.
Files:
Hostel.txt: Contains information about the hostel, such as name, rent, and available beds.
Student.txt: Stores details of students who have reserved a bed (name, roll number, address).
 
