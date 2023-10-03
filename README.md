# File-Sharing-System

• **File Sharing System** made with Python Django Framework.

• **User 1**: Operation User

• **User 2**: Client User

# How to build

```
git clone ttps://github.com/Isha307/File-Sharing-System.git
cd File-Sharing-System/
cd file_sharing/
source venv/bin/activate
pip install -r requirements.txt
```
# Creating Database and Table

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

# URL Present

```
    1. admin/
    2. [name='home']
    3. register/ [name='register']
    4. login/ [name='login']
    5. file-list [name='file-list']
    6. user-list [name='user-list']
    7. download/<int:assignment_id>/ [name='download_file']
    8. file-list-encrypted [name='file-list-encrypted']
    9. verification/
    10. ^download/(?P<path>,)$
    11. ^media/(?P<path>.*)$

```

# Run on your Local machine

```
python manage.py runserver
```
Then visit http://localhost:8000 to view the app.
