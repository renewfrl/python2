#!/usr/bin/env python3

from flask_script import Manager
from flask import Flask
from task import check_alive

# use Flask framework
app = Flask(__name__)


manager = Manager(app)

@manager.command
def confidence_check():
    print("do someting")
    res = check_alive()
    # and print htem


if __name__ == "__main__":
    manager.run()
