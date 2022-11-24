#
#
def decor(func):
    result = dict()
    def wraps(a):
        if a in result:
            return result[a]
        result[a] = func(a)
        return result[a]
    return wraps

@decor
def func(num_1):
    return num_1**100000

# def func(num_1):
#     return num_1**100000
print(func(50))