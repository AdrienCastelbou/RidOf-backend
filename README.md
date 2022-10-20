<h1>Rid Of ♻️ — an educational application aimed at simplifying the process of recycling trash in your daily life.</h1>

![Ridof](https://user-images.githubusercontent.com/82381064/196823050-8fdee47b-6c70-4147-a301-0b7a4f5360f4.png)



<p>
Frontend repo : https://github.com/Rayane-T/RidOf_UI </br>
Developed during //Slash Hack '22
</p>

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

7. DL one pretrained model, for example [yolo.h5](https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0/)

8. copy and rename .env.example to .env and fill it, with the path of your model
```bash
$ cp .env.example .env
``` 

9. Run the server
```bash
$ python server.py
```

10. Try to access to it at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
