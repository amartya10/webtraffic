import csv
import logging

def read_csv(path) -> list:
    rows = []
    logging.info("CSV file read path {}".format(path))
    with open (path , "r" ) as file:
        csv_reader = csv.reader(file)
        # ignore header line
        next(csv_reader)
        for row in csv_reader:
            rows.append(row)

    return rows