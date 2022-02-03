# from .. import Constants
import os
import pickle
import streamlit as st

filename_instruction = "..\\Pickles\\pickle_instruction"
filename_response = "..\\Pickles\\pickle_response"


def main():
    st.write('Simple Calculator')
    x = st.number_input('X')
    y = st.number_input('Y')

    operation = None
    text = None

    # Addition
    button_addition = st.button('Addition', help='Calculate the '
                                                 'sum of X and Y')
    if button_addition:
        operation = 'add'
        text = f'{x} + {y} = '

    # Subtraction
    button_subtraction = st.button('Subtraction', help='Calculate the '
                                                       'difference of X '
                                                       'and Y')
    if button_subtraction:
        operation = 'sub'
        text = f'{x} - {y} = '

    # Multiplication
    button_multiplication = st.button('Multiplication', help='Calculate the '
                                                             'product of X '
                                                             'and Y')
    if button_multiplication:
        operation = 'mult'
        text = f'{x} * {y} = '

    # Division
    button_division = st.button('Division', help='Calculate the '
                                                 'quotient of X and Y')
    if button_division:
        operation = 'div'
        text = f'{x} / {y} = '

    # If any button pressed:
    if operation is not None:
        instruction = (x, y, operation)
        with open(filename_instruction, "wb") as filepointer:
            pickle.dump(instruction, filepointer)

        os.system("..\\Chai-Backend\\env\\Scripts\\activate && python "
                  "..\\Chai-Backend\\main.py")

        with open(filename_response, "rb") as filepointer:
            result = pickle.load(filepointer)
            st.write(text + str(result))


main()

