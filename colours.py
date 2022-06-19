class Color():

    def __init__(self,red,green,blue,text):
        self.red = red
        self.green = green
        self.blue = blue
        self.text = text
    
    def get_color_escape(self,red,green,blue):
        return '\033[{};2;{};{};{}m'.format(38,red,green,blue)

    def print_colour(self):
        # Creates the coloured text and returns it
        all_coloured = self.get_color_escape(self.red,self.green,self.blue) + self.text + "\033[0m"
        return all_coloured

# Red Text
def colour_red(message):
    return Color(255, 107, 107, message).print_colour()
# Green Text
def colour_green(message):
    return Color(107, 255, 107, message).print_colour()
# Orange Text
def colour_orange(message):
    return Color(255, 181, 107, message).print_colour()
# Gray Text
def colour_gray(message):
    return Color(107, 107, 107, message).print_colour()
# Blue Text
def colour_blue(message):
    return Color(107, 181, 255, message).print_colour()
# Yellow Text
def colour_yellow(message):
    return Color(255, 255, 107, message).print_colour()
# Pink Text
def colour_pink(message):
    return Color(255, 107, 255, message).print_colour()
# Purple Text
def colour_purple(message):
    return Color(181, 107, 255, message).print_colour()