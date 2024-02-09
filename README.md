# Django CustomUser App

## This is a Django project named Codemonk, which includes three apps: Accounts, Codemonk, and Newapp.

# Table of Contents
  - Codemonk
      - Accounts
      - Codemonk
      - Newapp
  - requirements.py
  - DOCKERFILE
  - docker-compose.yaml
# Brief of the Contents
  - **Codemonk.Accounts**
      - This Django app provides a custom user model named `CustomUser` that extends `AbstractBaseUser` and `PermissionsMixin`. The app includes a custom manager named `UserManager` for user-related operations.
      ## Custom User Model(models.py)
      ### Fields
      
      - **id**: Auto-incremented primary key.
      - **name**: User's name.
      - **email**: User's email address (unique).
      - **dob**: User's date of birth.
      - **is_active**: Boolean field indicating whether the user account is active.
      - **is_staff**: Boolean field indicating whether the user has staff privileges.
      - **createdAt**: Date field representing the user's creation date.
      - **modifiedAt**: Date field representing the last modification date.
      ## UserManager(manager.py)
        - This creates a user based on customuser model and save it to database
        - This helps to create users with limited permissions
        - This also helps to create super users
  - **Codemonk.Newapp**
       - This Django app contains the Paragraphs and Wordmap models which stores paragraphs in database and wordmap based on paragraphs and also provides rest apis
       - **models.py**
           - This creates the Paragraphs and wordmap models
       - **urls.py**
           - This provides the accessible urls
       - **views.py**
           - **login_page**
               - Here authentication is done based on email and password
           - **register**
               - Here form data is accessed and new user is registered using some paramters like email,name,password
           - **get_paras**
               - Here a word is entered by user and through querying the database we find the paras which contains the word
           - **post_paragraphs**
               - Here we insert paragraphs to its unique id and map the words to the para id in the database
   - **Codemonk.codemonk**
         - This is the main app of the Django Application .
         - **textparser.py**
               - These is used to create a textparser which is used when text is passes as a request in /post_para api.
         - **settings.py**
               - This is where the custom user model created is imported here
               - This contains the apps needed to be added like newapp,accounts
               - This is where we specify the postgres database . Here we mention the database name,user,host,password,port
               - Here we also specify parsers for form parsing and plaintext parser and also the json parser
    - **requirements.txt**
       - this file contains the modules required to run this project along with the required versions
 # Requirements
   - python : 3.10.2
   - pip
   - postman
   - pycharm
   - venv
   - pgAdmin4
# Installation
  - Clone the project in your local directory
  - Ensure that venv is installed
  - activate enviroment using venv/Scripts/activate.ps1 in pycharm terminal 
  - Ensure that all the requirements of the modules are satisfied
  - Create a Postgresql database named paragraphs and change the connection parameters in newapp.views.py
  - use python manage.py makemigrations
  - use python manage.py migrate
  - user python manage.py runserver to use the apis

               - 
               
     
    
