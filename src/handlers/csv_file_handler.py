
import os
import pandas as pd

from src.services.flights_data import ROOT_DIR


OUTPUT_DIR = os.path.join("data", "csv_output")


def save_to_cvs(data):
    """
    Saves data in a csv file.
    :param data: A list of flights data.
    """
    is_created = False
    while not is_created:
        try:
            file_name = input("Please enter the file name: ")
            file_address = os.path.join(ROOT_DIR, OUTPUT_DIR, file_name+".csv")
            df = pd.DataFrame(data)
            df.to_csv(file_address, index=False)
            print("File created successfully.")
            print(f"File address {OUTPUT_DIR}")
            is_created = True
        except Exception as e:
            print(e)