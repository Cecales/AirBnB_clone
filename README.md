![AirBnB](https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)
# 0x00. AirBnB clone - The console
## Background Context
### Welcome to the AirBnB clone project!
Before starting, please read the [AirBnB](https://intranet.hbtn.io/concepts/66) concept page.
##### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

+ put in place a parent class (called **BaseModel**) to take care of the initialization, serialization and deserialization of your future instances
+ create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
+ create all classes used for AirBnB (**User**,**State**, **City**, **Place**…) that inherit from **BaseModel**
+ create the first abstracted storage engine of the project: File storage.
+ create all unittests to validate all our classes and storage engine

#### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

+ Create a new object (ex: a new User or a new Place)
+ Retrieve an object from a file, a database etc…
+ Do operations on objects (count, compute stats, etc…)
+ Update attributes of an object
+ Destroy an object

### Resources
**Read or watch:**

+ [Python abstract classes](https://blog.teclado.com/python-abc-abstract-base-classes/)
+ [cmd module](https://docs.python.org/3.4/library/cmd.html)
+ Packages concept page
+ [uuid module](https://docs.python.org/3.4/library/uuid.html)
+ [datetime](https://docs.python.org/3.4/library/datetime.html)
+ [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
+ [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
+ [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google:**

### General
+ How to create a Python package
+ How to create a command interpreter in Python using the **cmd** module
+ What is Unit testing and how to implement it in a large project
+ How to serialize and deserialize a Class
+ How to write and read a JSON file
+ How to manage **datetime**
+ What is an **UUID**
+ What is ***args** and how to use it
+ What is ****kwargs** and how to use it
+ How to handle named arguments in a function

## Requirements
### Python Scripts
+ Allowed editors: **vi, vim, emacs**
+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
+ All your files should end with a new line
+ The first line of all your files should be exactly **#!/usr/bin/python3**
+ A **README.md** file, at the root of the folder of the project, is mandatory
+ Your code should use the pycodestyle (version 2.7.*)
+ All your files must be executable
+ The length of your files will be tested using **wc**
+ All your modules should have a documentation **(python3 -c 'print(__import__("my_module").__doc__)')**
+ All your classes should have a documentation **(python3 -c 'print(__import__("my_module").MyClass.__doc__)')**
+ All your functions (inside and outside a class) should have a documentation **(python3 -c 'print(__import__("my_module").my_function.__doc__)'** and **python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')**
+ A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
+ Allowed editors: **vi, vim, emacs**
+ All your files should end with a new line
+ All your test files should be inside a folder **tests**
+ You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest) 
+ All your test files should be python files (extension: **.py**)
+ All your test files and folders should start by **test_**
+ Your file organization in the tests folder should be the same as your project
+ e.g., For **models/base_model.py**, unit tests must be in: **tests/test_models/test_base_model.py**
+ e.g., For **models/user.py**, unit tests must be in: **tests/test_models/test_user.py**
+ All your tests should be executed by using this command: **python3 -m unittest discover tests**
+ You can also test file by file by using this command: **python3 -m unittest tests/test_models/test_base_model.py**
+ All your modules should have a documentation **(python3 -c 'print(__import__("my_module").__doc__)')**
+ All your classes should have a documentation **(python3 -c 'print(__import__("my_module").MyClass.__doc__)')**
+ All your functions (inside and outside a class) should have a documentation **(python3 -c 'print(__import__("my_module").my_function.__doc__)'** and **python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')**
+ We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## More Info
### Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
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
```
All tests should also pass in non-interactive mode: **$ echo "python3 -m unittest discover tests" | bash**


## Supported Commands
Name |	Description |	Use |
-----|--------------|-------|
help |	Displays help information for a command |	help [command]
quit |	Exits/quits the program | quit
EOF | Exits the program when files are passed into the program | N/A
create | Creates a new instance of a specified class | create [class_name]
show | Prints the string representation of an instance | show [class_name] [id]
destroy | Deletes an instance | destroy [class_name] [id]
all | Prints the string representation of all instances of a class | all or all [class_name] [id]
update | Adds or modifies attributes of an instance | update [class_name] [id] [attribute] [value]-

## Classes you can use
All Classes |	Description
------------|-----------------------
User |	Class User, that inherits from BaseModel and contains specific public attributes
State |	Class State, that inherits from BaseModel and contains specific public attributes
City | Class City, that inherits from BaseModel and contains specific public attributes
Amenity | Class Amenity, that inherits from BaseModel and contains specific public attributes
Place | Class Place, that inherits from BaseModel and contains specific public attributes
Review | Class Review, that inherits from BaseModel and contains specific public attributes

## Example

```
(hbnb) create User
82ba33d4-cba0-4cf7-8546-b99fd4c9aa47
```
```
(hbnb) show User 82ba33d4-cba0-4cf7-8546-b99fd4c9aa47
[User] (82ba33d4-cba0-4cf7-8546-b99fd4c9aa47) {'id': '82ba33d4-cba0-4cf7-8546-b99fd4c9aa47', 'created_at': datetime.datetime(2022, 3, 8, 14, 49, 17, 438479), 'updated_at': datetime.datetime(2022, 3, 8, 14, 49, 17, 438580)}
```
```
(hbnb) all
["[BaseModel] (79488505-c072-4211-b3fd-4c3f04394e2e) {'id': '79488505-c072-4211-b3fd-4c3f04394e2e', 'created_at': datetime.datetime(2022, 3, 7, 21, 43, 8, 32524), 'updated_at': datetime.datetime(2022, 3, 7, 21, 43, 8, 32577), 'name': 'My First Model', 'my_number': 89}", "[BaseModel] (62fe56fa-ff13-4a5c-b88f-3a61287a5089) {'id': '62fe56fa-ff13-4a5c-b88f-3a612|87a5089', 'created_at': datetime.datetime(2022, 3, 7, 23, 36, 27, 657448), 'updated_at': datetime.datetime(2022, 3, 7, 23, 36, 27, 657455), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (ea9a34ec-11cb-446a-b231-1df733e96d09) {'id': 'ea9a34ec-11cb-446a-b231-1df733e96d09', 'created_at': datetime.datetime(2022, 3, 7, 23, 38, 32, 503128), 'updated_at': datetime.datetime(2022, 3, 7, 23, 38, 32, 503136), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (54e4b9ac-d571-42b5-a6b1-44b1250873a4) {'id': '54e4b9ac-d571-42b5-a6b1-44b1250873a4', 'created_at': datetime.datetime(2022, 3, 7, 23, 40, 42, 202115), 'updated_at': datetime.datetime(2022, 3, 7, 23, 40, 42, 202129), 'name': 'My_First_Model', 'my_number': 89}", "[User] (6b9761a1-716c-452b-97ab-ae763c1372c8) {'id': '6b9761a1-716c-452b-97ab-ae763c1372c8', 'created_at': datetime.datetime(2022, 3, 8, 1, 44, 38, 491739), 'updated_at': datetime.datetime(2022, 3, 8, 1, 44, 38, 491749), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (799ae5b9-c013-45d6-8bcc-98cc094db62a) {'id': '799ae5b9-c013-45d6-8bcc-98cc094db62a', 'created_at': datetime.datetime(2022, 3, 8, 1, 44, 38, 492141), 'updated_at': datetime.datetime(2022, 3, 8, 1, 44, 38, 492151), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[BaseModel] (a6cecdc9-7cf1-4859-942f-4b4584cf956d) {'id': 'a6cecdc9-7cf1-4859-942f-4b4584cf956d', 'created_at': datetime.datetime(2022, 3, 8, 2, 2, 35, 779123), 'updated_at': datetime.datetime(2022, 3, 8, 2, 2, 35, 779215)}", "[BaseModel] (975619e3-cc24-4456-95e0-f1088a376215) {'id': '975619e3-cc24-4456-95e0-f1088a376215', 'created_at': datetime.datetime(2022, 3, 8, 2, 3, 32, 594913), 'updated_at': datetime.datetime(2022, 3, 8, 2, 3, 32, 595005)}", "[User] (98fd4406-e981-47d0-af5e-c8e1188f57a3) {'id': '98fd4406-e981-47d0-af5e-c8e1188f57a3', 'created_at': datetime.datetime(2022, 3, 8, 14, 48, 9, 394305), 'updated_at': datetime.datetime(2022, 3, 8, 14, 48, 9, 394385)}", "[User] (82ba33d4-cba0-4cf7-8546-b99fd4c9aa47) {'id': '82ba33d4-cba0-4cf7-8546-b99fd4c9aa47', 'created_at': datetime.datetime(2022, 3, 8, 14, 49, 17, 438479), 'updated_at': datetime.datetime(2022, 3, 8, 14, 49, 17, 438580)}"]
```
```
(hbnb) update BaseModel 79488505-c072-4211-b3fd-4c3f04394e2e name 'Betty'
(hbnb) show BaseModel 79488505-c072-4211-b3fd-4c3f04394e2e
[BaseModel] (79488505-c072-4211-b3fd-4c3f04394e2e) {'id': '79488505-c072-4211-b3fd-4c3f04394e2e', 'created_at': datetime.datetime(2022, 3, 7, 21, 43, 8, 32524), 'updated_at': datetime.datetime(2022, 3, 7, 21, 43, 8, 32577), 'name': 'Betty', 'my_number': 89
```
```
(hbnb) destroy BaseModel 79488505-c072-4211-b3fd-4c3f04394e2e
(hbnb) show BaseModel 79488505-c072-4211-b3fd-4c3f04394e2e
** no instance found **
```

