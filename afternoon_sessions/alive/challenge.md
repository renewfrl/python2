# Check the keep alive

* use the boiler plate software
* first run pip install -r requirements

## Final Goal
    * Read from a file the domains you want to do a confidence check
    * Each keep a live is checked
    * Result is written back to a file with the last check date - time + reponse time
    * If domain does not respond within 10 seconds (think of timeout) write down in file and shwo on screen
              

## First challege:

Request a single domain to see if it is alive

## Second challenge

Print this to a CSV file

## Challenge 3: 

Read the domains you want to check from a file 

# Hints

* __use the boilerplate code__
* to run a command in manager.py go the boilerplate directory
   ```bash
    python3 manager.py confidence_check
 
```
