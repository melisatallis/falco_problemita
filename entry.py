class Entry:
    """
    Entry class.
    Properties of input string.
    Method that checks for parenthesis errors.
    """

    # Global properties:
	#   string:         input string
	#   list:           list of characters in string
	#   len:            length of characters 
	#   char_values:    list of tuples (character, character value)

    def __init__(self, string):
        """Constructs an entry object."""
        self.string = string
        self.list = list(string)
        self.len = len(self.list)
        self.char_values = self.set_char_values()
        return

    def char_value(self, char):
        """Outputs a value for character."""
        # Internal function
        if char == "(":
            value = 1
        elif char == ")":
            value = -1
        else:
            value = 0
        return value

    def set_char_values(self):
        """
        Outputs a list of possible tupples:
            (char, value) = ("(",1), ("(",-1), or (other char, 0)
        """
        values = []
        for char in self.list: 
            values.append((char, self.char_value(char)))
        return values

    def check_parenthesis(self):
        """
        Checks for hanging parenthesis by calculating the total value of the string.
        """
        i = 0
        total_value = 0 
        while (i < self.len) & (total_value >= 0):
            total_value += self.char_values[i][1]
            i += 1
        if i < self.len:
            output = "Error: parenthesis closed without opening at position: " + str(i-1)
        elif total_value != 0:
            output = "Error: parenthesis not closed"
        else:
            output = "No parenthesis errors found"
        return output

my_string = Entry("((fika)dhdhdh)(hah())(hahash))(jjjaskdk)")
print(my_string.check_parenthesis())