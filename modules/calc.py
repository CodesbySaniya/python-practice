# if __name__ == "__main__"   "__name__ is a special built-in variable in Python. When a Python file is executed directly, __name__ is set to '__main__'. When the file is imported as a module, __name__ is set to the module's name. We use if __name__ == "__main__": to ensure that certain code, such as testing or the main program logic, runs only when the file is executed directly and not when it is imported."




print("__name__ =", __name__)

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Calculator is running directly")
