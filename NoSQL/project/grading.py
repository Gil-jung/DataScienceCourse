from pymongo import MongoClient
import sys

def pagination():
    #problem A

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def letter():
    #problem B

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

def perfect():
    #problem C

    for item in result:
        print('{ ', end='')
        for (k, v) in sorted(item.items()):
            print('{}:{}'.format(k, v), end=', ')
        print('\b\b }')

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2

    raw_input = sys.argv[1]
    #TODO  

    client.close()
