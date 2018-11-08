#To run: python hello.py from the terminal

# Simply imports Flask from the package flask
from flask import Flask

# Creates an instance of the Flask object using our module's name as a parameter.
# Flask uses this to resolve resources, and in complex cases, one can use
# something other than __name__ here. This links our module to the Flask object.
app = Flask(__name__)

# Python decorator. Flask uses decorators for URL routing
#they call a function that takes the function defined under the decorator
#(in our case, index()) and returns a modified function.
@app.route("/")

   # define a very simple function that returns our message. As this function
   # is called by Flask when a user visits our application, the return value of
   # this will be what is sent in response to a user who requests our landing
   # page.
   def index():
       return "Hello, World!"

   # conditional statement that evaluates to True if our application is run
   # directly. It is used to prevent Python scripts from being unintentionally
   # run when they are imported into other Python files.
   if __name__ == '__main__':
       # The final line kicks off Flask's development server on our local
       # machine. We set it to run on port 5000 (we'll use port 80 for
       # production) and set debug to True, which will help us see detailed
       # errors directly in our web browser.
       app.run(port=5000, debug=True)
