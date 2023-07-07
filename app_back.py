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

def leyendo_csv():
    pass

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
	# read csv
	# uploaded_df = pd.read_csv(data_file_path, encoding='unicode_escape')
	with open(data_file_path, 'r') as file:
		dict_general = {}
		count = 0
  
		reader = csv.reader(file, skipinitialspace=True)
		reader_dict = csv.DictReader(file, skipinitialspace=True)
		for row in reader:
			if count == 0:
				for col in row:
					dict_general[col] = []
					# print(col)
				count = count + 1
				print(dict_general)

		for register in reader_dict:
			print(dict(register))
				#for llave in row:
				#	print(llave)
					#if llave in dict_general:
					#	dict_general[llave].append()

	# Converting to html Table
	'''
 	uploaded_df_html = uploaded_df.to_html()
	return render_template('show_csv_data.html',
						data_var=uploaded_df_html)
	'''
	return 'Hola Mundo!'

if __name__ == '__main__':
	app.run(debug=True)
