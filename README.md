Overview of the AirBnB project.

1st piece is the console. It is where we'll be creating objects and learning about file serialization and also where we'll be creating our 1st storage engine, file storage.

The next piece will be the HTML: this is where we will learn how to make things look pretty and give a visual interface for the future user.

The 3rd piece is MySQL. It's where we will be learning a different type of storage. It's a type of database where we'll be able to find unique ways to store objects.

The next piece will be how to deploy HTML with fabric. It's where you'll be able to upload all the things we've made to the servers.

The 5th piece, the flask web application server, is where we'll be taking the models in storage, and we'll be able to integrate them with HTML.

The 6th piece is REST API. Here, we'll be taking things that are in object form and putting them into JSON.

The last piece will be the web dynamic, where we'll take the JSON API and integrate it with HTML to share the web application.


For The Console project:-

The shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$


But also in non-interactive mode:

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


All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
