csvfile = 'data.csv'

def read_csv(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        rows = file.readlines()
        rows = list(map(lambda x:x.strip(), rows))
        for row in rows:
            row = row.split(',')
            data.append(row)
    return data

data = read_csv(csvfile)

def get_all():
    return data

def get_row(row):
    return data[row]

def get_column(column):
    column_list = []
    for row in data:
        column_list.append(row[column])
    return column_list

def get_cell(row, column):
    return data[row][column]



# get_all() #Returns list of whole data/table
# get_column(0) # Returns list of whole first column
# get_row(0) # Returns list of whole first row
print(get_cell(0,0)) # Returns first cell value