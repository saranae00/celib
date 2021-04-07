import random
from celib.common import set_random_seed

if __name__ == "__main__":

    def set_random_list():
        list_random = []
        for _ in range(10):
            list_random.append(random.randint(0, 20))
        print(list_random)

    set_random_list()
    set_random_list()

    set_random_seed()
    set_random_list()
    set_random_seed()
    set_random_list()
