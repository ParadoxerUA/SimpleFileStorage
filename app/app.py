import os

from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from config import DebugConfig

app = Flask(__name__)
app.config.from_object(DebugConfig)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        print(request.files["file"])
        # POSTing without form
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # No selected file 
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(request.url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()

