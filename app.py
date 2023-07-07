import pandas as pd
from flask import *
import os
from werkzeug.utils import secure_filename

from helpers.functions import reading_csv, reading_dict, total_balance, transactions_for_month, average_amount

UPLOAD_FOLDER = os.path.join('static', 'uploads')

# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)

# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'This is your secret key to utilize session in Flask'

        
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
    
    # Obtaining general dict from csv
    keys_dict = reading_csv(data_file_path)
    csv_to_dict = reading_dict(data_file_path, keys_dict)

    # Balance
    total_balance(csv_to_dict)
            
    # Transactions
    transactions_for_month(csv_to_dict)
    
    # Average
    average_amount(csv_to_dict)
    
    return make_response(jsonify({'message': csv_to_dict}), 200)

if __name__ == '__main__':
	app.run(debug=True)
