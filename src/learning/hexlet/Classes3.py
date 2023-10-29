from lxml import etree


class A:
    def simple_func(self):
        print("Simple Function")

    def who(self):
        print('A')

    def test(self):
        A.who(self)


class B(A):
    def who(self):
        print('B')


obj = B()
obj.simple_func()  # Это вызовет ошибку, потому что Python пытается передать self в simple_func
obj.test()  # 'A'


class HTMLElement:
    def __init__(self):
        self.body = None

    def set_text_context(self, body):
        self.body = body

    def __str__(self):
        if not self.body:
            return f'<{self._params["name"]}>'
        else:
            return f'<{self._params["name"]}>{self.body}</{self._params["name"]}>'


class HTMLBrElement(HTMLElement):
    _params = {
        'name': 'br',
        'pair': False
    }


class HTMLDivElement(HTMLElement):
    # BEGIN (write your solution here)
    _params = {
        'name': 'div',
        'pair': False
    }

    def __init__(self):
        super().__init__()
    # END


class Sanitizer:
    # BEGIN (write your solution here)
    def sanitize(self, text):
        return text.strip()
    # END


def strip_tags(tag_string):
    parser = etree.HTMLParser()
    tree = etree.fromstring(tag_string, parser)
    return etree.tostring(tree, encoding='unicode', method='text')


class SanitizerStripTagsDecorator:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer

    # BEGIN (write your solution here)
    def sanitize(self, text):
        return self.sanitizer.sanitize(strip_tags(text))


# END


class Application:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer

    def run(self, text):
        return self.sanitizer.sanitize(text)


from abc import ABC, abstractmethod


class Enumerable(ABC):
    @abstractmethod
    def get_iterator(self):
        raise NotImplementedError("Subclasses must implement this method")

    # BEGIN (write your solution here)
    def max_by(self, order_key):
        iterator = self.get_iterator()
        if iterator:
            return max(iterator, key=order_key)
        else:
            return None
    # END


class Lesson:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration


class Course(Enumerable):
    def __init__(self, lessons):
        self.lessons = lessons

    def get_iterator(self):
        return self.lessons


lessons = [
    # Второй параметр это продолжительность урока в минутах
    # Lesson('react start', 3),
    # Lesson('react component', 9),
    # Lesson('react lifecycle', 2),
    # Lesson('redux', 4),
]

## Course() использует миксину Enumerable
course = Course(lessons)

lesson = course.max_by(lambda l: l.get_duration())
print(lesson)  # ('react component', 9)


