import pandas as pd

import os

if not os.path.exists("currentReceipts.csv"):
    csv = pd.DataFrame(columns=['Name','Email','Phone Number','Purchase'])
    csv.to_csv("currentReceipts.csv")
    print("File not found and created")
else:
    print("File already exists and will be ammended")

