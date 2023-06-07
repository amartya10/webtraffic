
from reader import read_csv
import sys
import getopt
import csv

import logging

logging.basicConfig(level=logging.INFO)


def read_request(request: list) -> tuple:
    if (len(request) >= 3 ):
        user = request[1]
        page = request[2]
        return (user,page)

def sliding_window(elements: list, window_size: int ) -> list:
    window = []
    if len(elements) == window_size:
       window.append(",".join(elements))
       return window
    for i in range(len(elements) - window_size + 1):
        window.append(",".join(elements[i:i+window_size]))
    return window

def get_user_visited_sequence(requests: list) -> dict: 
    """ from reques"""
    user_visited = {}
    for request in requests:
        user,page = read_request(request)
        if user != None and page != None:
            if user not in user_visited:
                user_visited[user] = []
            user_visited[user].append(page)
    logging.info("User count: {}".format(len(user_visited.keys())))
    return user_visited

def get_sequence_count(user_visited: dict, sequence_count: int) -> dict:
    results = {}
    for sequence in user_visited.values():
        sequence_length = len(sequence)
        unique_sequences = set()
        if sequence_length >= sequence_count:
            windows = sliding_window(sequence, sequence_count)
            unique_sequences.update(windows)
            for sequence in unique_sequences:
                if sequence not in results:
                    results[sequence] = 0
                results[sequence] +=1
    results = dict(sorted(results.items(), key= lambda x: -x[1]))
    return results

def log_result(result: dict) -> None:
    logging.info("--result--")
    for sequence, count in result.items():
        print("{}:{}".format(sequence, count))
    logging.info("!--result--")


def main():
    file_path = "./resource/default.csv"
    sequence_count = 3
    argv = sys.argv
    argv_len = len(argv)
    if (argv_len == 1):
        logging.info("Using Default CSV file and Sequence Count value 3")
    elif (argv_len == 3):
        file_path = argv[1]
        sequence_count = int(argv[2])
    else:
        print("help how to run  \n 1] If no argument pass defult csv file and sequnce count used (./resouce/default.csv ,3) \n\t python src/main.py  \n 2] For custom input \n\t python src/main.py file_path sequnece_count \n\t Example: python src/main.py ./resource/default.csv 2 ")
        return 0
    logging.info("file_path:{}, sequence_count:{}".format(file_path,sequence_count))
    reqs = read_csv(file_path)
    user_visits = get_user_visited_sequence(reqs)
    logging.info("user_visits:{}".format(user_visits))


    result = get_sequence_count(user_visits ,sequence_count)
    log_result(result)

if __name__ == "__main__":
    main()