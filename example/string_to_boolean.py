from celib.common import string_to_boolean

if __name__ == "__main__":
    str_bool = "yes"
    print(str_bool + " to boolean:" + str(string_to_boolean(str_bool)))
    str_bool = "no"
    print(str_bool + " to boolean:" + str(string_to_boolean(str_bool)))
    str_bool = "1"
    print(str_bool + " to boolean:" + str(string_to_boolean(str_bool)))
    str_bool = "0"
    print(str_bool + " to boolean:" + str(string_to_boolean(str_bool)))
    str_bool = "tRuE"
    print(str_bool + " to boolean:" + str(string_to_boolean(str_bool)))
    str_bool = "fAlSe"
    print(str_bool + " to boolean:" + str(string_to_boolean(str_bool)))
    str_bool = "not bool"
    print(str_bool + " to boolean:" + str(string_to_boolean(str_bool)))
