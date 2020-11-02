# assignment-scrapping

# Scrapping Data
This Project aims at scrapping data from website using python, selenium and mongodb. You need to install mongodb in system. In this project mongodb collections will be generate and other part is csv file will get downloaded. I completed this project by using python's selenium and django.
# Requirements to Run the Application on Localhost
<b> Dependencies </b>

Project requires:

- Python (>= 3.6)
- Django (>= 3.0)
- selenium

<b> Repository Cloning Using Gitbash </b>

To fetch the source code from the git to your local machine,we need to run the below mentioned command git bash


```
https://github.com/sameerajmera/assignment-scrapping.git
```

<b> Packages Installation </b>

Install the requirement.txt file using below command.
```
pip install -r requirements.txt
```

<b> Command to Run the Application on LocalHost Server </b>

Run the below mentioned command from your python terminal and your server will be open on localhost with port 8000 as it is hosted on Djnago Web app.

```
python manage.py runserver
```

# REST API

The REST API is described below.

## Step to Consume APIs on Postman

### Request
Enter the below url by selcting method = GET in postman tab
```
GET http://localhost:8000/
```
Downlodable CSV File will be generate which will contain all the infornmation regarding data
