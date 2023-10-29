import os


class FileError(Exception):
    pass


class NotExistsError(FileError):
    pass


class NotReadableError(FileError):
    pass


class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        filepath = self.filepath

        # BEGIN (write your solution here)
        if not os.path.exists(filepath):
            raise NotExistsError(f"'{filepath}' does not exist")
        elif not os.access(filepath, os.R_OK):
            raise NotReadableError(f"'{filepath}' does not read")
        # END
        with open(filepath, 'r') as file:
            return file.read()


def read_files(files_path):
    result = []
    for file_path in files_path:
        file = File(file_path)
        try:
            result.append(file.read())
        except FileError:
            result.append(None)
    return result


values = read_files([r'C:\projects\prj3\python\nechaev_python_api\src\learning\hexlet\file', '/etc/unknown'])
print(values)  # => ["какие-то данные", None]

# file = File(r'C:\projects\prj3\python\nechaev_python_api\src\learning\hexlet\file')
# print(file.read())  # "какие-то данные"

# file = File('/etc/nonexists')
# print(file.read())  # NotExistsError
#
# file = File('/etc/shadow')
# file.read()  # NotReadableError
