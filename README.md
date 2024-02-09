<h1 align="center">HolbertonBnB</h1>
<p align="center">AirBnB clone.</p>

<p align="center">
	<img src="https://github.com/Bikaze/AirBnB_clone/blob/main/misc_stuff/hbnb.png" alt="HolbertonBnB logo">
</p>

---

## Project Description

This project is a clone of the Famous "AirBnB" website (But it doesn't exactly look like it :smile:)<br>
Hbnb(this project) is a fully fledged Web application, with a database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

**Currently**
- The project implements the back-end console(Command Interpreter)

## Command Interpreter(Backend-console) :man_technologist:

This first step is very important because what is built during this step will be used with all other
following steps: HTML/CSS templating, database storage, API, front-end integration…

**What will be the Use of this Console?**

-To create your data model
-Manage (create, update, destroy, etc) objects via a console / command interpreter
-Store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

<p align="center">
    <img src="">
</p>

**How to use the Console?**

The shell should work like this in interactive mode:

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

But also in non-interactive mode:

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
