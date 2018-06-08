import pandas as pd
import matplotlib.pyplot as plt
import os


def imp_file(file_name):
    """break-up file name into the root and the extension, then select just the extension"""
    extension = os.path.splitext(os.path.basename(file_name))[1]

    """choose file import method based on the extension and create variable to hold the data"""
    if extension == '.csv':
        data_frame = pd.read_csv(file_name)
        return data_frame
    elif extension == '.xlsx':
        sheet = input("What is the sheet name?")
        data_frame = pd.read_excel(file_name, sheet_name=sheet)
        return data_frame
    else:
        print("You need an excel or csv file!")


def get_col(data):
    """return a list of the column headers to display"""
    return list(data.columns)


def pvt_df(data_frame, pvt_value, pvt_index):
    """create a pivot table based on the parameters provided by input in main function"""
    pivot_df = pd.pivot_table(data_frame, values=pvt_value, index=pvt_index)
    return pivot_df


def plot_name(file):
    file_name = file.upper()
    root_name = os.path.splitext(os.path.basename(file))[0].upper()
    user_input = int(input("What would you like to name your graph? \n"
                           "1. Name of the file: {} \n"
                           "2. Root name of the file: {} \n"
                           "3. Custom name".format(file_name, root_name)))
    if user_input == 1:
        return file_name.upper()
    elif user_input == 2:
        return os.path.splitext(os.path.basename(file_name))[0].upper()
    elif user_input == 3:
        return input("Enter custom name: ").upper()
    else:
        return file_name.upper()


def create_plot(pivot, plot_color, plt_name):
    """creates plot based on pivot table with a title from the file name"""
    pivot.plot.bar(color=plot_color)
    plt.title(plt_name)
    plt.show()
