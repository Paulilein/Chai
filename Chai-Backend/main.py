# This is the backend
import pickle

filename_instruction = "..\\Pickles\\pickle_instruction"
filename_response = "..\\Pickles\\pickle_response"


def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiplicate(x, y):
    return x * y


def divide(x, y):
    return x / y


operation_dict = {
            'add': add,
            'sub': substract,
            'mult': multiplicate,
            'div': divide
        }


def main():
    with open(filename_instruction, "rb") as filepointer:
        x, y, operation = pickle.load(filepointer)
        result = operation_dict[operation](x, y)
    print(result)
    with open(filename_response, "wb") as filepointer:
        pickle.dump(result, filepointer)
    print('I did this too')


main()