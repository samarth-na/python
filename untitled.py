example_string = "qw\ter\tty\tui"
example_list = ["qw", "er", "ty", "ui"]
example_tuple = ("qw", "er", "ty", "ui")
example_dict = {"qw": "er", "ty": "ui"}


def string_methods():
    print(example_string.endswith("8,9"))
    print(example_string.expandtabs(1))
    print(example_string.expandtabs(2))
    print(example_string.expandtabs(3))
    print(example_string.expandtabs(4))


def main():
    string_methods()


##########################

if __name__ == "__main__":
    main()
