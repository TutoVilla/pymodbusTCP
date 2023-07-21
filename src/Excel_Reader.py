import pandas as pd
import numpy as np


class Excel_Functions():

    @classmethod
    def verified_doc(self, file_path, columns_to_verify):
        try:
            data = pd.read_excel(file_path, engine="openpyxl")

            # Check if all the specified columns are present in the DataFrame
            if all(column in data.columns for column in columns_to_verify):
                print(f"The Excel file has the correct structure ({', '.join(columns_to_verify)} columns).")
                return True
            else:
                print("The Excel file does not have the correct structure.")
                return False
        except Exception as e:
            print("Error reading the Excel file:", str(e))
            return False

        
    @classmethod
    def organize_data(cls, file_path,data_to_send):
        try:
            data = pd.read_excel(file_path)
            print(data)
            data_list = np.array(data[data_to_send].tolist())  
            return data_list
        
        except Exception as e:
            print("Error reading the Excel file:", str(e))
              
        