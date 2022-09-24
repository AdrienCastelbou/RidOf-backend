# RidOf-backend Quickstart

How to setup and launch the server and its environnement

## Setup

1. If you dont have Python installed, install it from [here](https://www.python.org/downloads/)

2. Clone this repository 
```bash
$ git clone https://github.com/AdrienCastelbou/RidOf-backend
```

3. Navigate into the project directory
```bash
$ cd RidOf-backend
```

4. Create a new virtual environment
```bash
$ python -m venv venv
$ source venv/bin/activate
```

5. Install the requirements (depending on your OS, uncomment the right lines in requirements.txt)
```bash
$ pip install -r requirements.txt
```

6. Install imageai without dependencies
```bash
$ pip3 install --no-deps imageai
``` 

7. Run the server
```bash
$ python server.py
```

9. Try to access to it at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
