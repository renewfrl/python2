#!/usr/bin/env python3

from flask_script import Manager
from flask import Flask
from task_handler import check_certs, print_results_to_screen, print_result_to_csv

# use Flask framework
app = Flask(__name__)


manager = Manager(app)

@manager.command
def check_certificates_screen():
    res = check_certs()
    print_results_to_screen(res)

@manager.command
def check_certificates_csv():
    res = check_certs()
    print_result_to_csv(res)


if __name__ == "__main__":
    manager.run()
