from celib.common import list_chunk

if __name__ == "__main__":
    list_full = []
    for i in range(10):
        list_full.append(i)

    print(list_full)

    list_split = list_chunk(list_full, 4)
    print(list_split)
