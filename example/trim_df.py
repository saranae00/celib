import pandas as pd
from celib.common import trim_df

if __name__ == "__main__":
    df = pd.DataFrame({"A": ["1  ", "  4", " 7"], "B": [2, 5, 8], "C": [" 3", "6", " 9   "]})
    print(df)
    print(trim_df(df))
