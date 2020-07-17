import os
from flask import Blueprint, render_template, request, flash, redirect, current_app, send_from_directory, make_response, jsonify
from werkzeug.utils import secure_filename
from models import File

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
            expiration_date = request.form['expiration_date']
            print(expiration_date)
            new_filename = File.add_file(file.filename, expiration_date)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], str(new_filename)))
            return make_response(jsonify({"data": {"Download URL": "127.0.0.1:5000/files/" + str(new_filename)}}))

    return render_template('index.html')

@bp.route('/files/<file_id>', methods=('GET', 'POST'))
def download_file(file_id):
    try:
        file = File.get_file(file_id)
    except FileNotFoundError:
        abort(404)
    
    print("OK!")
    if request.method == 'POST':    
        return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename=str(file.id),
        as_attachment=True, attachment_filename=file.filename)
        
    return render_template('filepage.html', expiration_time=file.expiration_time.strftime("%Y-%m-%d %H:%M:%S"))



