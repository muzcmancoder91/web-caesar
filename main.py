from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="POST">
        
        <label>Rotate by:
          <input type="text" name="rot" value="0">
        </label>
        
        <textarea name="text">{0}</textarea>
        
        <input type="submit" value="Submit Query" />
      </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format('')

@app.route('/', methods=["POST"])
def encrypt():
    # Store values from request parameters in local variables
    rot = int(request.form["rot"])
    text = request.form["text"]

    # Encrypt text and return
    encrypted_text = cgi.escape(rotate_string(text, rot))
    return form.format(encrypted_text)
    

app.run()