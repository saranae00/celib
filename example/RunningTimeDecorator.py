import logging
from celib.common import RunningTimeDecorator

log_file_name = "log.log"
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_file_name)

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s:%(name)s:%(asctime)s] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    handlers=[stream_handler, file_handler],
)
logger = logging.getLogger("RunningTimeDecorator")


# logger 사용
@RunningTimeDecorator(logger=logger, show_section=True, show_pid=True)
def func1(x, y):
    for i in range(10000000):
        y += x
    return y


# print 사용
@RunningTimeDecorator()
def func2(x, y):
    for _ in range(10000000):
        y += x
    return y


if __name__ == "__main__":
    result_a = func1(2, 3)
    print("Result of func1(2,3) : %s", result_a)
    result_b = func2(3, 4)
    print("Result of func2(3,4) : %s", result_b)
