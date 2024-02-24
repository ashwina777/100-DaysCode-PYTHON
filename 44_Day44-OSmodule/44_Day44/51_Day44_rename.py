import os

path = r"C:\Users\Amit rana\Documents\Data Science\python 100 days of code\44_Day44-OSmodule" 
data_path = os.path.join(path, "data")

for i in range(0, 5):
    os.rename(os.path.join(data_path, f"Tutorial{i+1}"),os.path.join(data_path, f"TutorialNo{i+1}"))
