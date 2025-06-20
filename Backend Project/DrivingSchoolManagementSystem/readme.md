# Design and development of driving school reservation learning system based on SSM

## 1、Project Introduction

The driving school reservation management system based on SSM1 has three roles, namely administrator, coach, and student. 
The specific functions are as follows:

- Administrator: student management, coach management, driving school vehicle management, reservation management, cancellation management, announcement management

- Coach: coach information query, reservation management, cancellation management, registration, personal center

- Student: view coach information, make an appointment with a coach, cancel an appointment with a coach, evaluate a coach, register, personal center



## 2、Project Technology

Backend framework: SSM (Spring, SpringMVC, Mybatis)

Frontend framework: Bootstrap, vue, jsp, css, JavaScript, JQuery

Frontend and backend separation project

## 3、Development Environment

- JAVA version: JDK1.8
- IDE type: Intelligi IDEA
- tomcat version: Tomcat 7.5
- Database version: MySql 5.7
- Hardware environment: Windows 10


## 4、Function Introduction

### 4.1 Log in

![Front-end login](https://www.codeshop.fun/Typora-Images/20220514223433.jpg)

Coaches and students can log in to the front-end system through this interface

### 4.2 Student Module

![Student Personal Center](https://www.codeshop.fun/Typora-Images/20220514223517.jpg)

![Students query coach information 1](https://www.codeshop.fun/Typora-Images/20220514223523.jpg)

![Students view coach information 2](https://www.codeshop.fun/Typora-Images/20220514223529.jpg)

![Students make an appointment with a coach](https://www.codeshop.fun/Typora-Images/20220514223536.jpg)

![Student Backstage-Appointment Management](https://www.codeshop.fun/Typora-Images/20220514223541.jpg)

![Student backend-cancel appointment management](https://www.codeshop.fun/Typora-Images/20220514223546.jpg)

- View coach information: students can filter coaches by coach account and name, and query coach details

- Make an appointment with a coach: students can make an appointment with a coach, and can fill in the time and subject on the appointment interface (see video for details)

- Make an appointment and cancel an appointment: students can check appointment information and cancel appointments in their own backend

- Register and personal center: students can register and modify personal information

- Evaluate a coach: students can evaluate a coach


### 4.3 Coaching Module

![Coach Backstage-Coach Information Query](https://www.codeshop.fun/Typora-Images/20220514223853.jpg)

![Coach backend appointment management](https://www.codeshop.fun/Typora-Images/20220514223855.jpg)

![Cancel appointment management in coach backend](https://www.codeshop.fun/Typora-Images/20220514223858.jpg)

- Coach information query: Coaches can query other coach information details by account number and name

- Appointment management: Coaches can query student appointment information details by appointment number

- Cancel appointment management: Coaches can cancel student appointment applications and query cancellation records


### 4.4 Administrator Module

![Administrator-Driving School Vehicle Management](https://www.codeshop.fun/Typora-Images/20220514224054.jpg)

![Administrator-Driving School Announcement Management](https://www.codeshop.fun/Typora-Images/20220514224058.jpg)

![Administrator-Driving School Instructor Management](https://www.codeshop.fun/Typora-Images/20220514224100.jpg)

![Administrator-Student Management](https://www.codeshop.fun/Typora-Images/20220514224103.jpg)

![Administrator-Appointment Management](https://www.codeshop.fun/Typora-Images/20220514224108.jpg)

![Admin-Cancel Appointment Management](https://www.codeshop.fun/Typora-Images/20220514224111.jpg)

- Coach management: Administrators can filter coach information by account and name, and can add, view, modify, delete coaches, and view coach evaluations

- Student management: Administrators can filter student information by account, name, and gender, and can add, view, modify, and delete students

- Driving school vehicle management: Administrators can filter vehicles by license plate number, and can add, view, modify, and delete vehicles

- Appointment management: Administrators can filter student appointment record information by appointment number, and can view, modify, and delete records

- Cancel appointment management: Administrators can filter cancel appointment record information by appointment number and coach account, and can view, modify, and delete records

- Announcement management: Administrators can query announcements by title, and can add, view, modify, and delete announcements


