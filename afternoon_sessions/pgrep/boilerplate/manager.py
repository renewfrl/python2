#!/usr/bin/env python3

from flask_script import Manager, Command
from flask import Flask
from task import whatever

# use Flask framework
app = Flask(__name__)


manager = Manager(app)

#./manager.py name_of_command 1 2 3 4 5
@manager.add_command
class PyGrepCommand(Command):
    name = 'name_of_command'
    capture_all_args = True

    def run(self, remaining):
        print(remaining)


if __name__ == "__main__":
    manager.run()
