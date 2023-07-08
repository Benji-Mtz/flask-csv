from flask import *
import os, random, json
from werkzeug.utils import secure_filename
import psycopg2

from helpers.functions import reading_csv, reading_dict, total_balance, transactions_for_month, average_amount
from init_db import create_table, get_db_connection

UPLOAD_FOLDER = os.path.join('static', 'uploads')

app = Flask(__name__)

# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'This is your secret key to utilize session in Flask'

create_table()
        
@app.route('/', methods=['GET', 'POST'])
def uploadFile():
	print("HOLA desde docker")
 
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
    conn = ''
	# Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
    
    # Obtaining general dict from csv
    keys_dict = reading_csv(data_file_path)
    csv_to_dict = reading_dict(data_file_path, keys_dict)

    # Balance
    tb = total_balance(csv_to_dict)
            
    # Transactions
    transactions = transactions_for_month(csv_to_dict)
    
    # Average
    debit, credit = average_amount(csv_to_dict)
    
    print(tb, transactions, debit, credit)
    
    id_cliente = random.randint(1,1000)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        postgres_insert_query = """ INSERT INTO transactions (id_client, t_balance, tx_for_month, avg_debit, avg_credit) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (id_cliente, tb, json.dumps(transactions), debit, credit,)
        cursor.execute(postgres_insert_query, record_to_insert)
        
        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into transactions table")
        
    except(Exception, psycopg2.Error) as error:
        print("Failed to insert record into transactions table", error)
        
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    
    return make_response(jsonify({'message': csv_to_dict}), 200)

if __name__ == '__main__':
	app.run(debug=True)
