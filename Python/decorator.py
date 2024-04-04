def wrapperFunction(function):
    print("Before Function!")
    def wrap(*args, **kwargs):
        result = function(*args, **kwargs)
        return result
    print("After Function!")
    return wrap

@wrapperFunction
def insideFunc():
    print("Inside Function!")
    return 1

insideFunc()