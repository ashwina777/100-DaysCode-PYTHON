import os

path = r"C:\Users\Amit rana\Documents\Data Science\python 100 days of code\44_Day44-OSmodule"  # Replace "/path/to/data" with your desired path
# in path we use r before the string to make it raw string so that we can use backslash in the path. we use blackslash in windows path
data_path = os.path.join(path, "data")
# os.path.join is used to join the path and the folder name to create a new path. it append the folder name to the path and thus create a new folder 
if not os.path.exists(data_path):
    os.mkdir(data_path)

for i in range(0, 5):
    os.mkdir(os.path.join(data_path, f"Day{i+1}"))
