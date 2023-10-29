class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes if attributes else {}

    def _stringify_attributes(self):
        print(self.attributes.items())
        line = ''.join(f' {k}="{v}"' for k, v in self.attributes.items())
        return line


class HTMLPairElement(HTMLElement):

    def __init__(self, attributes=None):
        super().__init__(attributes)
        self.body = ''

    def set_text_content(self, body):
        self.body = body

    def get_text_content(self):
        return self.body


class HTMLDivElement(HTMLPairElement):
    def __str__(self):
        return f'<div{self._stringify_attributes()}>{self.get_text_content()}</div>'


# END
div = HTMLDivElement({'name': 'div', 'data-toggle': 'true'})
div.get_text_content()
div.set_text_content('Body Text')
div.get_text_content()  # Body Text
print(div)  # => '<div name="div" data-toggle="true">Body Text</div>'

from abc import ABC, abstractmethod


class HTMLElement(ABC):
    ATTRIBUTE_NAMES = ['name', 'class']

    def __init__(self, attributes=None):
        if attributes is None:
            attributes = {}
        self.attributes = attributes

    @classmethod
    def get_attribute_names(cls):
        return cls.ATTRIBUTE_NAMES

    def get_attributes(self):
        return self.attributes

    # BEGIN (write your solution here)
    @abstractmethod
    def is_valid(self):
        pass
    # END


class HTMLButtonElement(HTMLElement):
    ATTRIBUTE_NAMES = ['type']
    TYPE_NAMES = ['button', 'submit', 'reset']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
        attrs = self.get_attributes()
        attr_names = self.get_attribute_names()
        for attr_name in self.ATTRIBUTE_NAMES:
            if attrs.get(attr_name) not in self.TYPE_NAMES:
                return False
        for key, value in attrs.items():
            if key not in attr_names:
                return False
        return True


button1 = HTMLButtonElement({'class': 'rounded', 'type': 'button'})
print(button1.is_valid())

button2 = HTMLButtonElement({'class': 'rounded'})
print(button2.is_valid())
