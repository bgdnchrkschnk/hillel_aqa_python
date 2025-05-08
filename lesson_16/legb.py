str = "global string" # global variable

def print_string():

    str = "nonlocal string"

    def print_it():

        global str
        str = "global string 2"
        print(str)


    print_it()

if __name__ == "__main__":
    print_string()
    print(str)

# LEGB L-local, E-enclosing (nonlocal), G - global, Built in