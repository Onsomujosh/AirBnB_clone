Description of the project
=================================================================================
hbnb is the first step towards building our first full web application.

In this initial step, we are going to build a console which will be a foundation
for future projects such as HTML, CSS, Front end integration etc

Description of the console
==================================================================================

The console is the interface we'll build to help us interact with
backend functions.

The console will help us manage the following objects in our project.

	1. Create a new object (ex: a new User or a new Place)
	2. Retrieve an object from a file, a database etc…
	3. Do operations on objects (count, compute stats, etc…)
	4. Update attributes of an object
	5. Destroy an object

Description of the commandline interpreter
====================================================================================
The interpreter uses the cmd class which helps us interact in
both interactive and non-interactive modes.

How to start it
-----------------------------------------------------------------------------------
Python3 is already installed in the unix shell. Run the following command to help
in starting it: python 3

All your python scripts should start with this line.

#!/usr/bin/python3

Typing an EOF character such as control-Cat the primary prompt causes the interpreter
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


Tests
=======================================================================================

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

Classes
=======================================================================================================

This project utilizes the following classes: BaseModel, FileStorage, User, State, City, Amenity,
Place, Review

FileStorage
========================================================================================================

The FileSorage class implements the file storage in this project. The data is stored in json.






















