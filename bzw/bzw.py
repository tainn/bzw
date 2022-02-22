import os


class Bzw:
    """Allows for creation of bzw objects and writing them to a file."""

    def __init__(self, filename: str, overwrite: bool = False) -> None:
        """Sets the name of the bzw file.

        :param filename: desired name of the bzw file
        :param overwrite: optional kwarg whether to overwrite an existing file or not
        """
        self.filename: str = set_filename(filename=filename, overwrite=overwrite)

    def create(self, ref: str, group: bool = False, **kwargs) -> None:
        """Creates and appends the specified object to a bzw file.

        :param ref: object reference
        :param group: bool whether the object is a group or not
        :param kwargs: object attributes and their values
        """
        with open(self.filename, 'a') as f:
            f.write(f'{ref}\n' if not group else f'group {ref}\n')

            for attr in kwargs:

                if type(kwargs[attr]) is list or type(kwargs[attr]) is tuple:
                    kwargs[attr] = ' '.join(map(str, kwargs[attr]))

                f.write(f'{attr} {kwargs[attr]}\n')

            f.write('end\n\n')

    def define(self, name: str = None, end: bool = False) -> None:
        """Creates an opening or closing line of a group definition.

        :param name: name of the definition object
        :param end: bool whether it is the end of the definition or not
        """
        with open(self.filename, 'a') as f:
            f.write(f'define {name}\n\n' if not end else 'enddef\n\n')

    def include(self, path: str) -> None:
        """Creates an include line.

        :param path: path to the included file
        """
        with open(self.filename, 'a') as f:
            f.write(f'include {path}\n\n')

    def emptyline(self, amount: int = 1) -> None:
        """Creates the specified amount of empty lines.

        :param amount: amount of empty lines to create
        """
        with open(self.filename, 'a') as f:
            f.write('\n' * amount)

    def comment(self, content: str, addline: bool = False) -> None:
        """Creates a comment with the passed content.

        :param content: content of the comment
        :param addline: bool whether to add an extra newline or not
        """
        with open(self.filename, 'a') as f:
            f.write(f'# {content}\n' if not addline else f'# {content}\n\n')


def set_filename(filename: str, overwrite: bool = False) -> str:
    """Finds and sets the name of the bzw file.

    :param filename: desired name of the bzw file
    :param overwrite: optional kwarg whether to overwrite an existing file or not
    :return: the end filename that is applied
    """
    initial_candidate: str = filename if filename.endswith('.bzw') else f'{filename}.bzw'
    candidate: str = initial_candidate
    postfix_increment: int = 1

    while True:
        if os.path.isfile(candidate) and not overwrite:
            candidate: str = f'{initial_candidate.split(".bzw")[0]}-{str(postfix_increment).zfill(2)}.bzw'
            postfix_increment += 1

        elif os.path.isfile(candidate) and overwrite:
            os.remove(candidate)
            break

        else:
            break

    return candidate
