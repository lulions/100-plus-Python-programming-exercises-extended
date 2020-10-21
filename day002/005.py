class StringIO:
    text = "No string specified"

    def get_string(self):
        self.text = input("Insert a string: ")

    def print_string(self):
        print(self.text)


stringio = StringIO()
stringio.print_string()
stringio.get_string()
stringio.print_string()
