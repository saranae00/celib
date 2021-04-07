import logging
import pandas as pd
from celib.common import RunningTimeDecorator, parallelize_dataframe, parallelize_dataframe_with_args

log_file_name = "log.log"
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_file_name)

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s:%(name)s:%(asctime)s] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    handlers=[stream_handler, file_handler],
)
logger = logging.getLogger("parallelize_dataframe")


@RunningTimeDecorator(logger)
def add1(df):
    df["result"] = df["A"] + df["B"]
    return df


@RunningTimeDecorator(logger)
def add2(df, cnt):
    df["result"] = df["A"] + df["B"] + cnt
    return df


if __name__ == "__main__":
    df = pd.DataFrame(
        [
            {"A": "a", "B": "b"},
            {"A": "c", "B": "b"},
            {"A": "a", "B": "g"},
            {"A": "z", "B": "b"},
            {"A": "e", "B": "b"},
            {"A": "a", "B": "g"},
            {"A": "a", "B": "n"},
            {"A": "a", "B": "p"},
            {"A": "a", "B": "q"},
            {"A": "j", "B": "h"},
        ]
    )
    parallelize_dataframe_result = parallelize_dataframe(add1, df)
    logger.info("parallelize_dataframe_result")
    print(parallelize_dataframe_result)

    parallelize_dataframe_with_args_result = parallelize_dataframe_with_args(add2, df, "3")
    logger.info("parallelize_dataframe_with_args_result")
    print(parallelize_dataframe_with_args_result)
