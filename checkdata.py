import sys
import pandas as pd

def read_sheet(path):
    new_data = pd.read_csv(path)
    print (new_data.head(10))
    return new_data

if __name__ == "__main__":
    df = read_sheet(sys.argv[1])
