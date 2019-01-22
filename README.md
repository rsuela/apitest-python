# apitest - assignments

A script that contains Python unittest code for validating the given API endpoint.

## Getting Started

These instructions will guide you from downloading a copy of the project to running it on your local machine.

### Prerequisites

1. Download and Install Python 2.7 (also works with Python 3.x)
    * Select the appropriate installer for your machine. see [Python 2.7.15](https://www.python.org/downloads/release/python-2715/)
 
2. Install Python requests module
 ```
 easy_install pip
 pip install requests
 ```
 
Thats it!

## Download the zip file of the repository
1. On your browser, go to https://github.com/rsuela/apitest-python
2. Click on the "Clone or Download" button then click "Download ZIP"
3. Extract the zip to any location. (i.e C:/ or /tmp)

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
 
 After running the command the result should look something like below. This means that all the tests has passed.
 ```
 [root@ilocalmachine apitest-python]# python test_categories.py 
...
----------------------------------------------------------------------
Ran 3 tests in 1.443s

OK
```

## Troubleshooting
1. I get the following error when running the script.
```
[root@localmachine apitest-python]# python test_categories.py 
Unable to connect to https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false
```
Answer: Make sure that the machine has an internet connection and able to access the endpoint.

2. After installing Python, I came across this error when I try to install requests.
```
[root@localmachine apitest-python]# easy_install pip
bash: easy_install: command not found
```

```
[root@localmachine apitest-python]# pip install requests
bash: pip: command not found
```

Answer: Your Python installation is missing the pip or easy_install module. Run the following commands to install PIP.

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Then run the following:

```
python get-pip.py
```


## Authors

* **Rey Angelo Suela**
