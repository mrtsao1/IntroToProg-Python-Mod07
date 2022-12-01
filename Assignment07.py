'''
Title: Assignment 07
Description: Simple examples demonstrating pickling and error handling
Change Log: (Who, When, What)
MTsao, 2022-11-27, Created File
MTsao, 2022-11-28, Created Example #1 demonstrate pickling only
MTsao, 2022-11-29, Created Example #2 pickling with error handling
'''

import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    """  Save data to binary file
    :return: nothing
    """
    pass
    objFile = open(file_name, "wb+")
    pickle.dump(list_of_data, objFile)
    objFile.close()
    print("Data has been saved to \"" + file_name + "\".")

def read_data_from_file(file_name):
    """  Read data from binary file
    :return: nothing
    """
    pass
    try:
        objFile = open(file_name, "rb+")
        objFileData = pickle.load(objFile)  # load() only loads one row of data.
        objFile.close()
        print("Data stored in \"" + file_name + "\":")
        print(objFileData)
    except FileNotFoundError as e: # file does NOT exist
        print("Data file must exist before running this script!")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')

def calculate_quotient():
    """  Calculate quotient, save to .txt file
    :return: nothing
    """
    try:
        intNumerator = int(input("Enter numerator: "))
        intDenominator = int(input("Enter denominator: "))
        quotient = intNumerator / intDenominator
        new_file_name = input("Enter the name of the file you want to save to: ")
        if new_file_name.isnumeric(): # number was entered for filename
            raise Exception('Do not use numbers for the file\'s name')
        f = open(new_file_name, 'r+')  # the read plus option gives an error if filed does not exist
        f.write(str(quotient))  # causes an error if the file does not exist
        f.close()
        print("Data successfully saved to\"" + new_file_name + "\"!")
    except ZeroDivisionError as e: # division by zero
        print("Please do no use Zero for the second number!")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
    except FileNotFoundError as e: # good inputs, but file does NOT exist
        print("Text file must exist before running this script!")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e: # non-integer inputs (including no input)
        print("There was a non-specific error!")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')

def output_menu_tasks():
    """  Display a menu of choices to the user
    :return: nothing
    """
    print("\nExample #2: Error Handling and Raising Custom Errors\n")
    print("Menu of Options")
    print("1) Calculate quotient. Save Data to File")
    print("2) Read Data from File")
    print("3) Exit Program\n")

def input_menu_choice():
    """ Gets the menu choice from a user
    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
    print()  # Add an extra line for looks
    return choice

# Presentation ------------------------------------ #
'''Example #1: Pickling'''
# Get ID and NAME From user, then store it in a list object
print("Example #1: Pickling")
intId = int(input("Enter an Id: "))
strName = str(input("Enter a Name: "))
lstCustomer = [intId, strName]

# store the list object into a binary file
save_data_to_file(strFileName, lstCustomer)
input("\nPress enter when ready to continue")

# Read the data from the file into a new list object and display the contents
read_data_from_file(strFileName)

'''Example #2: Error Handling and Raising Custom Errors'''
input("\nPress enter when ready to continue")
while True:
    output_menu_tasks()  # Shows menu
    choice_str = input_menu_choice()  # Get menu option

    if choice_str.strip() == '1':  # Write Data to File
        print("Calculate quotient & save Data to File")
        calculate_quotient()
        continue  # to show the menu

    elif choice_str == '2':  # Read Data from File
        print("Read Data from File")
        strFileName = input("Enter filename: ")
        read_data_from_file(strFileName)
        continue  # to show the menu

    elif choice_str == '3':  # Exit Program
        print("Exiting Program. Goodbye!")
        input("Press any key to continue")
        break  # by exiting loop

    else:   # Invalid choice
        print("Invalid choice entered. Please try again.")
