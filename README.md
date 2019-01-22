# apitest - assignments

A script that contains Python unittest code for validating the given API endpoint.

## Getting Started

These instructions will guide you from downloading a copy of the project to running it on your local machine.

### Prerequisites

* Python 2.7.*
* GIT

### Setup

Clone the repository
 ```
git clone https://github.com/rsuela/apitest-python.git
 ```

Run the following commands to install the necessary Python modules to run the script.
 ```
 # In-case pip module is not installed
 easy_install pip
 
 cd apitest-python
 pip install -r requirements.txt
 ```
 
Thats it!


## Running the tests

The script contains 3 tests and it will validate the following acceptance criteria:

* Name = "Carbon credits"
* CanRelist = true
* The Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"

To execute the test, Run the following command:
 ```
 cd apitest-python
 python test_categories.py
 ```
 
 After running the command, the result should look something like below. This means that all the tests has passed.
![Console](https://s3.amazonaws.com/resources.reysuela.com/console.png "console")

A reports folder will be generated and will contain an HTML file containing the test results.

![html results](https://s3.amazonaws.com/resources.reysuela.com/htmlresult.png "HTML results")


## Troubleshooting
1. I get the following error when running the script.
```
[root@localmachine apitest-python]# python test_categories.py 
Unable to connect to https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false
```
Answer: Make sure that the machine has an internet connection and able to access the endpoint.


## Authors

* **Rey Angelo Suela**
