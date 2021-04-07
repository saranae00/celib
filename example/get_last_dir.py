from celib.common import get_last_dir

if __name__ == "__main__":
    print("get_last_dir by name: " + get_last_dir("./"))
    print("get_last_dir by ctime: " + get_last_dir("./", by="ctime"))
    print("get_last_dir by mtime: " + get_last_dir("./", by="mtime"))
    print("get_last_dir by atime: " + get_last_dir("./", by="atime"))
