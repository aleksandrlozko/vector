class Glass():

    """
    Provides methods for creating vector image like broken glass.
    """

    def __init__(self):

        """
        Initialize attributes with default values.
        """

        self.width = 0
        self.height = 0
        self.svg_list = []
        self.templates = self.generate_templates()


    def __str__(self):

        """
        Transforms list to string.
        """

        return("".join(self.svg_list))


    def add(self, text):

        """
        Adds element for drawing.
        """

        self.svg_list.append(str(text))


    def generate_templates(self):

        """
        Templates for construction.
        """

        templates = {}

        templates["create"] = "<svg width='{}px' height='{}px' xmlns='http://www.w3.org/2000/svg'>\n"
        templates["end"] = "</svg>"
        templates["line"] = "<line x1='{}' y1='{}' x2='{}' y2='{}' stroke='black' stroke-width='2' stroke-opacity='1' />\n"

        return templates


    def create(self, width, height):

        """
        Creates space at given width and height.
        Opens tag.
        """

        self.width = width
        self.height = height

        self.add(self.templates["create"].format(width, height))


    def line(self, x1, y1, x2, y2):

        """
        Builds vector at given coordinates.
        """

        self.add(self.templates["line"].format(x1, y1, x2, y2))


    def finish(self):

        """
        Closes tag.
        """

        self.add(self.templates["end"])


    def save(self, path):

        """
        Saves SVG file on the given path.
        """

        file = open(path, "w+")
        file.write(str(self))
        file.close()