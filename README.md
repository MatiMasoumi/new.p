You are tasked with creating a ToDo list manager using Object-Oriented Programming (OOP
). Your program should consist of at least three classes: Task, Manager, and a Main function for running the application. Each class should be in a separate file to manage the project more effectively.
Task Class: • Each task must have the following attributes: • A title (string). • A description (string). 
• A unique task ID, which should be a number but must be stored as a string (your program should check that the ID is numeric).
• Start time, which is automatically recorded when a task is created. • End time, which is recorded when the task is marked as done. 
- Status: A boolean value that is set to False when the task is created and set to True when the task is marked as done. = ToDo List OOP Project Manager Class:
- • The manager should be able to: • Add a task: Create and add a new task with a unique task ID. • Change task status to done: Mark the task as completed,
- update the status to True, and record the end time. • Display tasks: Show all tasks along with their details, such as task ID, title, description,
-  start time, end time (if completed), and current status (done or not done). • Task summary: Display the number of tasks that are completed
-   (status = True) and those that are not completed (status = False). ToDo List OOP Project main: • The manager should be able to: • The main function should interact with the Manager to allow user
-   s to perform actions such as adding a task, marking a task as done, and viewing all tasks. Additional Requirements: •
-   Your program must be split into at least three files: one for the Task class, one for the Manager class, and one for the Main. • Make sure task IDs are unique. •
-    Ensure your program can handle and display the task details correctly.




You are tasked with creating a system for managing electronic devices. Both Laptops and Smartphones share some common features, but they also have their own specific characteristics.
Use inheritance to avoid repeating code. Device Class (Base Class): • Common Attributes (shared by both laptops and smartphones): • Brand (string) • Model (string) • Price (float) 
• Common Methods: • Turn On: Prints a message that the device is powered on. • Turn Off: Prints a message that the device is powered off. • Display Info: Displays the brand, model,
and price of the device. 200 Question 01 (Inheritance) Laptop Class (Derived Class): • Inherits all attributes and methods from the Device class. • Additional Attribute: • RAM Size (integer, GB)
• Additional Method: • Open Laptop: Prints a message indicating the laptop is opened. Smartphone Class (Derived Class): • Inherits all attributes and methods from the Device class. • 
Additional Attribute: • Camera Resolution (integer, MP) • Additional Method: • Take Photo: Prints a message saying a photo has been taken.

