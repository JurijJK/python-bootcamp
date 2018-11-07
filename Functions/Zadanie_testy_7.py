x = lambda i: i == 4

def x(i):
    if i == 4:
        return True
    return False

#lambda jest znacznikiem dla napisania prostej funkcji żeby oszczędzić ilości kodu, np.: lambda x: x ==  * 2


data = [1,2,3,4,5,6,7]

start = lambda x: x > 3
stop = lambda x: x == 6

def przytnij(data, start, stop):
    result = []
    dodawac_do_listy = False
    for element in data:
        if start(element):
            dodawac_do_listy = True
        if dodawac_do_listy:
            result.append(element)
            if stop(element):
                break

    return result



def test_przytnij():
    assert przytnij(data = [1,2,3,4,5,6,7], start = lambda x: x > 3, stop = lambda x: x == 6) == [4, 5, 6]