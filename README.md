# BuyLegit

LANGUAGE VERSIONS
  python version - python3 3.9.2
  python interpreter version - python3 3.9.2 64-bit('venv') / python3 3.9.2 64-bit('env')


INSTALLATIONS
#FLASK
  Flask supports Python 3.5 and newer, Python 2.7, and PyPy.
    install Flask
    $ pip install Flask
    
Solve Cross Origin Resource Sharing with Flask
  pip install -U flask-cors
    
Connect with MySQL 
  pip install pymysql
  

1. INSTRUCTIONS FOR CREATE FLASK PROJECT
    1. Create a new project folder on your file system
    2. Open that project in command prompt to create a virtual environment named "env"
    3.    Enter below commands based on your interpreter
               # Linux
                sudo apt-get install python3-venv    # If needed
                python3 -m venv env
                
                # macOS
                python3 -m venv env

                # Windows
                python -m venv env
      4. Open the project folder in VS Code
      5. In VS Code, open the Command Palette and select the "Python: Select Interpreter"
      6. The command presents a list of available interpreters, then you can select Python Interpreter
      7. Update pip in the virtual environment
                python -m pip install --upgrade pip
      8. Install Flask in the virtual environment
                python -m pip install flask
      9. Inside the project create new python file and add code to import Flask and create an instance of the Flask object.
                from flask import Flask
                app = Flask(__name__)
      10. Add functions with app.route
      11. Save file and run the app
                python -m flask run


  