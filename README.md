# Spotify-Top-Track-Finder

## Starting the App

This app once its running only requires an genre input. This is the list of genres that the app can define:
* Rock
* Alternative Rock
* Pop
* Blues
* Country
* Electronic
* Jazz
* R&B
* Rap
* Raggae

Once the user type a correct genre the app will list 10 tracks of a artist in that genre.
The list of tracks are the top 10 song of that artist. These list are based of from US 
Music charts. Every track have a preview so that the user can listen a sample of the song.

## How to Run the App

#### Running Backend
For this application you must run the Django backend first. For that you must have These Libraries

* Python Dotenv
* Requests
* Django Rest Framework
* Django Serializers
* Django Cors Headers

An then when you run the server by

```
python manage.py runserver
```

It will run the backend Server.

#### Running Frontend

You must install the vue cli. For that you can use

```
npm install -g @vue/cli
```

Selecting only router and babel start the project. Then download the vue_app files from here

After that you need to install 'axios' and Bootstrap

```
npm install axios
```
```
npm install bootstrap
```
The app is ready to run. Write this comment to the terminal and the Frontend will run on localhost

```
npm run serve
```

