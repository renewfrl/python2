#!/usr/bin/env python3

from flask_script import Manager
from flask import Flask
from task import check_certs, print_results_to_screen, print_result_to_csv

# use Flask framework
app = Flask(__name__)


manager = Manager(app)

@manager.command
def check_certificates_screen():
    print("do someting")
    res = check_certs()
    # and print htem

@manager.command
def check_certificates_csv():
    print("do something too")



if __name__ == "__main__":
    manager.run()
