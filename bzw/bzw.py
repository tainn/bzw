import os


class Bzw:
    """Allows creation of bzw objects and writing them to a file."""

    def __init__(self, filename: str, overwrite: bool = False) -> None:
        self.filename: str = set_filename(filename=filename, overwrite=overwrite)

    def create(self, ref: str, group: bool = False, **kwargs) -> None:
        with open(self.filename, "a") as f:
            f.write(f"{ref}\n" if not group else f"group {ref}\n")

            for attr in kwargs:

                if type(kwargs[attr]) is list or type(kwargs[attr]) is tuple:
                    kwargs[attr] = " ".join(map(str, kwargs[attr]))

                f.write(f"{attr.strip('_')} {kwargs[attr]}\n")

            f.write("end\n\n")

    def define(self, name: str = None, end: bool = False) -> None:
        with open(self.filename, "a") as f:
            f.write(f"define {name}\n\n" if not end else "enddef\n\n")

    def include(self, path: str) -> None:
        with open(self.filename, "a") as f:
            f.write(f"include {path}\n\n")

    def emptyline(self, amount: int = 1) -> None:
        with open(self.filename, "a") as f:
            f.write("\n" * amount)

    def comment(self, content: str, addline: bool = False) -> None:
        with open(self.filename, "a") as f:
            f.write(f"# {content}\n" if not addline else f"# {content}\n\n")


def set_filename(filename: str, overwrite: bool = False) -> str:
    initial_candidate: str = filename if filename.endswith(".bzw") else f"{filename}.bzw"
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
