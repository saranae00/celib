import sys
from celib.common import get_last_path

if __name__ == "__main__":
    sys.path.append("../../")
    print("get_last_dir by name: " + get_last_path("./"))
    print("get_last_dir by ctime: " + get_last_path("./", by="ctime"))
    print("get_last_dir by mtime: " + get_last_path("./", by="mtime"))
    print("get_last_dir by atime: " + get_last_path("./", by="atime"))
    print("get_last_path by atime: " + get_last_path("./", type="file"))
    print("get_last_path by atime: " + get_last_path("./", type=".md"))
