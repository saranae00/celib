from celib.common import unnesting
import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame({"A": [1, 2], "B": [[1, 2], [3, 4]], "C": [[1, 2], [3, 4]]})
    print(df)
    result = unnesting(df, ["B", "C"])
    print(result)
