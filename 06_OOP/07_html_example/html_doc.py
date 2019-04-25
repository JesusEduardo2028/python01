class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE html', '')
        self.end_tag = ''


class Head(Tag):
    
    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        """Body contents will be built separately"""
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
        super().display(file=file)


class HtmlDoc(object):
    """Html doc class does not inherits from Body but it behaves the same as that class using composition"""

    def __init__(self, title=None):
        # Composition
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':

    my_page = HtmlDoc('Demo Html title')
    my_page.add_tag('h1', 'Main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    with open('composition.html', 'w') as test_doc:
        my_page.display(file=test_doc)


new_body = Body()
new_body.add_tag('h1', 'aggregation')
new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                      " of objects to build another objects")
new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of "
                      " - if its destroyed, those objects continue to exists.")


my_page._body = new_body

with open('aggregation.html', 'w') as test_doc:
    my_page.display(file=test_doc)

# Inheritance --> Is A
# Composition / Aggregation --> Has A
