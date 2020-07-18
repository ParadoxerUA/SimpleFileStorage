import os
from flask import Blueprint, render_template, request, flash, redirect, current_app, send_from_directory, make_response, jsonify
from werkzeug.utils import secure_filename
from models import File
from datetime import datetime, timedelta

bp = Blueprint('storage_blueprint', __name__)

@bp.route('/', methods=('GET', 'POST'))
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
            days = int(request.form['days'])
            hours = int(request.form['hours'])
            minutes = int(request.form['minutes'])
            expiration_time = datetime.now() + timedelta(days=days, hours=hours, minutes=minutes)

            new_filename = File.add_file(file.filename, expiration_time)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], str(new_filename)))
            return jsonify({"data": {"download_url": "http://127.0.0.1:5000/files/" + str(new_filename)}})

    return render_template('index.html')

@bp.route('/files/<file_id>', methods=('GET', 'POST'))
def download_file(file_id):
    try:
        file = File.get_file(file_id)
    except FileNotFoundError:
        abort(404)
    
    if request.method == 'POST':    
        return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename=str(file.id),
        as_attachment=True, attachment_filename=file.filename)

    expiration_time = file.expiration_time - datetime.now()
    expiration_time -= timedelta(microseconds=expiration_time.microseconds)
    return render_template('filepage.html', expiration_time=expiration_time)



