import csv

calendar = {
    '1': "Januray",
    '2': "Febrary",
    '3': "March",
    '4': "April",
    '5': "May",
    '6': "June",
    '7': "July",
    '8': "August",
    '9': "September",
    '10': "October",
    '11': "November",
    '12': "December"
}

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

def reading_dict(data_file_path, keys_dict):
    with open(data_file_path, 'r') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            for llave in row:
                keys_dict[llave].append(row[llave])
    return keys_dict


def total_balance(general_dict):
    
    for llave in general_dict:
        if 'Transaction' in llave:
            tb = sum([ float(value) for value in general_dict[llave]])
            print(tb)
        else:
            pass
    
def transactions_for_month(general_dict):
    dates = {}
    for llave in general_dict:
        if 'Date' in llave:
            dates = general_dict[llave]
        else:
            pass
            
    register_dates = {}
    default_day = 1
    
    for date in dates:
        month_int, _ = date.split('/')
        month_str = calendar[month_int]
        
        if month_str in register_dates:
            register_dates[month_str] = register_dates[month_str] + 1
        else:
            register_dates[month_str] = default_day
            
    print(register_dates)

def average_amount(general_dict):
    for llave in general_dict:
        if 'Transaction' in llave:
            liststr_to_float = [ float(value) for value in general_dict[llave]]
            debit = sum([ negative for negative in liststr_to_float if negative < 0]) / 2
            credit = sum([ positive for positive in liststr_to_float if positive >= 0 ]) / 2
            
            print(debit, credit)
        else:
            pass