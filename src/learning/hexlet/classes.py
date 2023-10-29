class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes if attributes else {}

    def get_attribute(self, key):
        return self.attributes.get(key)

    # BEGIN (write your solution here)
    def _stringify_attributes(self):
        result_string = ""
        for key, value in self.attributes.items():
            result_string += f' {key}=\"{value}\"'
        return result_string

    # END
    # BEGIN (write your solution here)
    def _stringify_attributes2(self):
        return ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        # END

    def add_tag(self, tag):
        values = self.get_attribute("tag").split(" ")
        if tag not in values:
            self.attributes["tag"] = " ".join([*values, tag])

    def remove_tag(self, tag):
        values = self.get_attribute("tag").split(" ")
        if tag in values:
            values.remove(tag)
            self.attributes["tag"] = " ".join(values)

    def toggle_tag(self, tag):
        values = self.get_attribute("tag").split(" ")
        if tag in values:
            self.remove_tag(tag)
        else:
            self.add_tag(tag)


class HTMLHrElement(HTMLElement):
    def __str__(self):
        return f'<hr{self._stringify_attributes()}>'


hr = HTMLHrElement()
expected = '<hr>'
print(expected == str(hr))

hr = HTMLHrElement()
print(str(hr))  # => <hr>

hr = HTMLHrElement({'class': 'w-75', 'id': 'wop'})
print(hr)  # => '<hr class="w-75" id="wop">'


class HTMLDivElement(HTMLElement):
    pass


div = HTMLDivElement({'tag': 'one two'})
print(div.get_attribute('tag'))  ## 'one two'

div.add_tag('small')
print(div.get_attribute('tag'))  ## 'one two small'

div.add_tag('small')
div.get_attribute('tag')  ## 'one two small'

div.remove_tag('two')
div.get_attribute('tag')  ## 'one small'

div.toggle_tag('small')
div.get_attribute('tag')  ## 'one'

div.toggle_tag('small')
div.get_attribute('tag')  ## 'one small'


class Base:
    # BEGIN (write your solution here)
    def is_instance_of(self, class_name):
        result = class_name in list(map(lambda cls: cls.__name__, self.__class__.mro()))
        print(result)
        return result
    # END


class Child(Base):
    pass


class ChildOfChild(Child):
    pass


obj = ChildOfChild()
obj.is_instance_of('Base')  ##  True
obj.is_instance_of('Child')  ## True
obj.is_instance_of('ChildOfChild')  ## True
obj.is_instance_of('SomeClass')  ## False

import os


class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_stat = os.stat(self.file_path)

    def get_size(self):
        return self.file_stat.st_size


class SmartFileInfo(FileInfo):

    def __init__(self, file_path):
        super().__init__(file_path)

    def get_size(self, volume_unit='b'):
        size = super().get_size()
        if volume_unit == 'b':
            return size
        elif volume_unit == 'kb':
            return size / 1024
        elif not volume_unit:
            return size
        else:
            raise ValueError()

