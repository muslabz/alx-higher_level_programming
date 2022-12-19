#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    ret = []
    while i < list_length:
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            new.append(0)
        except TypeError:
            print("wrong type")
            new.append(0)
        except IndexError:
            print("out of range")
            new.append(0)
        finally:
            ret.append(res)
            i += 1
        return ret


