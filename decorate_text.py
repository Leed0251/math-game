class Decorate_text():

    # Input for the main class e.g. Decorate_text(decororation,text)
    def __init__(self,decoration,text):
        self.decor = decoration
        self.text = text

    def surround(self,x,y):

        final_text = ""
        for item in range(0,y):
            # Add line of decoration
            final_text += self.decor*(x+len(self.text)+2+x) + "\n"

        final_text += "{} {} {}\n".format(self.decor*x,self.text,self.decor*x)

        for item in range(0,y):
            # Add line of decoration
            final_text += self.decor*(x+len(self.text)+2+x) + "\n"
        
        return final_text