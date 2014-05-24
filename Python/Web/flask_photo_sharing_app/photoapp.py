from flask import Flask, request,render_template
import settings
import os
from models import Image

app = Flask(__name__)

@app.route("/")
def show_Gallery():
    """Return a list of files contained in the directory pointed by settings.GALLERY_ROOT_DIR.
    """
    images = Image.all()
    return render_template('index.html', images=images)
    #return "hello world"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


