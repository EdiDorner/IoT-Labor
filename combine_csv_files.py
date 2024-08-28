### import libraries
import pandas as pd
import os


### get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


### define input csv file paths
resource_folder = os.path.join(script_dir, "resources")
car_file_path = os.path.join(resource_folder, "car.csv")
motorcycle_file_path = os.path.join(resource_folder, "motorcycle.csv")


### read csv files to data frames
car_df = pd.read_csv(car_file_path, sep=";")
motorcycle_df = pd.read_csv(motorcycle_file_path, sep=";")


### combine the data frames 
combination = pd.concat([car_df, motorcycle_df], axis=0)


### replace NaN-values with "unknown" 
endresult = combination.fillna("unknown")


### write the result to the file output.csv in the output folder
output_folder = os.path.join(script_dir, "output")  
output_file_name = "output.csv"
output_file_path = os.path.join(output_folder, output_file_name)

endresult.to_csv(output_file_path, index=False, sep=";")


### visualize
print("Endresult:\n", endresult)
