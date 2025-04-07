# LATESHOW
This is a Flask API that contains the details of a late night show. 

# DESCRIPTION
This Flask API has details on a late night show including, the guests that have appeared on the show, the episode in which these guests appear in the show and the rating of their appearance. 

# INSTALLATION

1. To install the program, clone the program to your local device by pasting the following command on your termainal, 
```sh 
git clone git@github.com:eddymwaniki/lateshow-eddy-maina.git
```
2. Once cloned to your local device, enter into the program's directory, paste the following on your terminal, 
```sh
cd lateshow-eddy-maina
```
3. Install all required dependecies, run 
```sh 
pipenv install
``` 
4. Enter into the project's shell through 
```sh 
pipenv shell
```
5. To set up the database run  
```sh 
flask db upgrade
``` 
6. Seed the database by running 
```sh 
python seed.py
```

# USAGE 

The Flask API can be run and tested on Postman.To get started, paste the following into your terminal:

```sh
export FLASK_APP=app.py  
export FLASK_RUN_PORT=5555
flask run
```  

Endpoints:

1. View all episodes: Send a **GET** request to

http://127.0.0.1:5555/episodes

2. View a specific episode: Send a **GET** request to

http://127.0.0.1:5555/episodes/(int)

3. View all guests: Send a **GET** request to

http://127.0.0.1:5555/guests

4. Create a appearance: Send a **POST** request to

http://127.0.0.1:5555/appearances

# AURTHOR 
.Eddy Mwaniki

# LICENCE
This program is an open source under the MIT license.