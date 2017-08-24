class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)




class Mylist(list, metaclass=ListMetaclass):
    pass



if __name__ == "__main__":
    l = Mylist()
    l.add(1)
    print(l)
