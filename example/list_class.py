from celib.common import ListClass


class Item:
    @property
    def prop(self):
        return self.__prop1

    def __init__(self, value) -> None:
        self.__prop1 = value


class ListTest(ListClass):
    def print_list(self):
        for item in self.list_class:
            print(item.__dict__)


if __name__ == "__main__":
    item1 = Item(3)
    item2 = Item(1)
    item3 = Item(7)
    item4 = Item(2)

    list_test = ListTest(list_class=[item1, item2, item3, item4])
    print("print_list")
    list_test.print_list()
    print("sort")
    list_test.sort("prop")
    list_test.print_list()
    print("find_node")
    print(list_test.find_node("prop", 3)[0].prop)
    print("contains_node")
    print(list_test.contains_node("prop", 3))
    print(list_test.contains_node("prop", 13))
