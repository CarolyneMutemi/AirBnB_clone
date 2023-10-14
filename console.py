#!/usr/bin/python3

"""
Contains the CMD program.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter.
    """
    prompt = '(hbnb)'

    def do_create(self, class_name):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not class_name:
            print("** class name missing **")
        elif shlex.split(class_name)[0] in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            class_Name = shlex.split(class_name)[0]
            new_obj = eval(class_Name)()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, class_plus_id):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if not class_plus_id:
            print("** class name missing **")
        elif shlex.split(class_plus_id)[0] not in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(shlex.split(class_plus_id)) > 1:
            class_name = shlex.split(class_plus_id)[0]
            obj_id = shlex.split(class_plus_id)[1]
            all_objs = storage.all()
            if f"{class_name}.{obj_id}" in all_objs.keys():
                print(all_objs[f"{class_name}.{obj_id}"])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, class_plus_id):
        """
        Deletes an instance based on the class name and id.
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not class_plus_id:
            print("** class name missing **")
        elif shlex.split(class_plus_id)[0] not in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(shlex.split(class_plus_id)) > 1:
            class_name = shlex.split(class_plus_id)[0]
            obj_id = shlex.split(class_plus_id)[1]
            all_objs = storage.all()
            if f"{class_name}.{obj_id}" in all_objs.keys():
                del all_objs[f"{class_name}.{obj_id}"]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, class_name):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        all_objs = storage.all()
        if not class_name:
            for v in all_objs.values():
                print(v)
        elif shlex.split(class_name)[0] in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            class_Name = shlex.split(class_name)[0]
            for v in all_objs.values():
                if v.__class__.__name__ == class_Name:
                    print(v)
        else:
            print("** class doesn't exist **")

    def do_update(self, class_plus_att):
        """
         Updates an instance based on the class name and id
         by adding or updating attribute (save the change into the JSON file).
         Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if not class_plus_att:
            print("** class name missing **")
        elif shlex.split(class_plus_att)[0] not in \
            ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(shlex.split(class_plus_att)) > 1:
            class_name = shlex.split(class_plus_att)[0]
            obj_id = shlex.split(class_plus_att)[1]
            all_objs = storage.all()
            if f"{class_name}.{obj_id}" in all_objs.keys():
                if len(shlex.split(class_plus_att)) > 2:
                    if len(shlex.split(class_plus_att)) > 3:
                        obj_attribute = shlex.split(class_plus_att)[2]
                        obj_att_value = shlex.split(class_plus_att)[3]
                        obj = all_objs[f"{class_name}.{obj_id}"]
                        obj.__dict__[obj_attribute] = obj_att_value
                        obj.save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_EOF(self, line):
        """
        EOF command to exit the program.
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
