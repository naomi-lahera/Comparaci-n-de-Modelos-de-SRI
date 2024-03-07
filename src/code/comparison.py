import csv

def obtain_column(column_name):
    
    """
    Reads two CSV files and extracts values from a specific column for each file.

    Args:
    column_name (str): Name of the column from which values will be extracted.

    Returns:
    list: A list of tuples containing the query ID and the column value for each CSV file.
        Each tuple is structured as ((id, column), (id, column)).
    """
    csv1, csv2 = 'Metricas_boolean.csv', 'Metricas_extended.csv'
    columns = {}

    # Validate that the column name is valid
    valid_column_names = ['Query ID', 'Precision', 'Recall', 'F-measure', 'F1-measure', 'Accuracy']
    if column_name not in valid_column_names:
        raise ValueError("The column name is not valid")

    # Read the first CSV file
    with open(csv1, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            query_id = row['Query ID']
            value = row[column_name]
            columns[query_id] = (query_id, value)

    # Read the second CSV file and update the dictionary
    with open(csv2, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            query_id = row['Query ID']
            value = row[column_name]
            if query_id in columns:
                columns[query_id] = (columns[query_id], (query_id, value))

    return columns.values()

result = obtain_column('Precision')
