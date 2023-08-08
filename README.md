Description of the project
=================================================================================
hbnb is the first step towards building our first full web application.

In this initial step, we are going to build a console which will be the foundation
for future projects such as HTML, CSS, Front end integration etc

Description of the console/commandline interpreter
==================================================================================

The console is the interface we'll build to help us interact with
backend functions. The 2 words (console and commandline interpreter) are used
interchangeably.

The console will help us manage the following objects in our project.

	1. Create a new object (ex: a new User or a new Place)
	2. Retrieve an object from a file, a database etc…
	3. Do operations on objects (count, compute stats, etc…)
	4. Update attributes of an object
	5. Destroy an object


The interpreter uses the cmd class which helps us interact in
both interactive and non-interactive modes.

How to start it
-----------------------------------------------------------------------------------
Python3 is already installed in the unix shell. Run the following command to help
in starting it: python 3

All your python scripts should start with this line.

#!/usr/bin/python3

Typing an EOF character such as control-C at the primary prompt causes the interpreter
to exit with a zero exit status.

How to use it
----------------------------------------------------------------------------------------
The shell should work in both intercative and non-interactive modes.
In interactive mode the commands are read from the tty.

The shell should work like this in interactive mode

	$ ./console.py
	(hbnb) help
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

But also in non-intercative mode

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

-------------------------------------------------------------------------------------------
Command interpreter commands

Python Scripts
=========================================================================================================

1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
3. All your files should end with a new line
4. The first line of all your files should be exactly #!/usr/bin/python3
5. A README.md file, at the root of the folder of the project, is mandatory
6. Your code should use the pycodestyle
7. All your files must be executable
8. The length of your files will be tested using wc
9. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
10. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
11. All your functions (inside and outside a class) 
	should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
	and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

Tests
=========================================================================================================

1. Allowed editors: vi, vim, emacs
2. All your files should end with a new line
3. All your test files should be inside a folder tests
4. You have to use the unittest module
5. All your test files should be python files (extension: .py)
6. All your test files and folders should start by test_
7. Your file organization in the tests folder should be the same as your project
	e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
	e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
8. All your tests should be executed by using this command: python3 -m unittest discover tests
9. You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
10. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
11. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
12. All your functions (inside and outside a class) should have a documentation 
	(python3 -c 'print(__import__("my_module").my_function.__doc__)' and
	python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

Classes
=======================================================================================================

This project utilizes the following classes: BaseModel, FileStorage, User, State, City, Amenity,
Place, Review

FileStorage
========================================================================================================

The FileSorage class implements the file storage in this project. The data is stored in json.






















