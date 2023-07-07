import pandas as pd
from flask import *
import os, csv
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join('static', 'uploads')

# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'This is your secret key to utilize session in Flask'

def reading_csv(data_file_path):
    with open(data_file_path, 'r') as file:
        diccionary_aux = {}
        count = 0
  
        reader = csv.reader(file, skipinitialspace=True)
        for row in reader:
            if count == 0:
                for col in row:
                    diccionary_aux[col] = []
					# print(col)
                count = count + 1
                return diccionary_aux

def reading_dict(data_file_path, general_dict):
    with open(data_file_path, 'r') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            for llave in row:
                general_dict[llave].append(row[llave])
    return general_dict

@app.route('/', methods=['GET', 'POST'])
def uploadFile():
	if request.method == 'POST':
	# upload file flask
		archive = request.files.get('file')

		if len(archive.filename) < 1:
			return render_template("index.html")

		else:
			# Extracting uploaded file name
			data_filename = secure_filename(archive.filename)

			archive.save(os.path.join(app.config['UPLOAD_FOLDER'],data_filename))

			session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)

			return render_template('index2.html')
	return render_template("index.html")


@app.route('/show_data')
def showData():
	# Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    
    general_dict = reading_csv(data_file_path)
    inserting_dict = reading_dict(data_file_path, general_dict)
    
    print(inserting_dict)


    return make_response(jsonify({'message': inserting_dict}), 200)

if __name__ == '__main__':
	app.run(debug=True)
