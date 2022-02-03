# Running the Application

To run the Application, it is recomneded to set some environment variables manually.

```
SECRET_KEY = <A secret key string>
SQLALCHEMY_DATABASE_URI = <path to the databse>
```

However, these aren't mandatory, as fallback keys will be used and the URI will be able to locate the databse by itself. 

Next, let Flask know where to find the app.
```
FLASK_APP=quizApp.py
```

Next, the libraries will need to be installed. To do this run the below command.
```
pip install -r requirements.txt
```

Once configured, run the app with `flask run`. From here, you should be able to go to the login page and login with users already in the database. 
```
username: tim
password: tim
```

Further, you can create your own user and login wiht that user. To create a user, access the login page and then click the link at the bottom. 
