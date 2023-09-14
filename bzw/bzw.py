import os
from typing import Any

from .exceptions import BadParamTypeError


class Bzw:
    def __init__(self, filename: str, overwrite: bool = False) -> None:
        self.filename: str = self._set_filename(
            name=filename,
            overwrite=overwrite,
        )
        self.content: str = ""

    @staticmethod
    def _set_filename(name: str, overwrite: bool = False) -> str:
        if not name.endswith(".bzw"):
            name = f"{name}.bzw"

        name_root: str = name.split(".bzw")[0]
        true_name: str = name
        postfix_inc: int = 1

        while True:
            if not os.path.isfile(true_name):
                break

            if overwrite:
                os.remove(true_name)
                break

            two_digit_postfix: str = str(postfix_inc).zfill(2)
            true_name = f"{name_root}-{two_digit_postfix}.bzw"
            postfix_inc += 1

        return true_name

    def create(self, type_: str, group: bool = False, **kwargs: Any) -> None:
        if group:
            self.content += f"group "

        self.content += type_
        self.emptyline(1)

        for key_ in kwargs:
            if not isinstance(kwargs[key_], (str, int, float, list, tuple)):
                raise BadParamTypeError(type(kwargs[key_]))

            reduced_param: Any = kwargs[key_]

            if isinstance(kwargs[key_], (list, tuple)):
                reduced_param = " ".join(map(str, kwargs[key_]))

            self.indent(2)
            self.content += f"{key_.strip('_')} {reduced_param}"
            self.emptyline(1)

        self.content += "end"
        self.emptyline(2)

    def define(self, name: str = "", end: bool = False) -> None:
        if not end:
            self.content += f"define {name}"
        else:
            self.content += "enddef"

        self.emptyline(2)

    def include(self, path: str) -> None:
        self.content += f"include {path}"
        self.emptyline(2)

    def comment(self, content: str) -> None:
        self.content += f"# {content}"
        self.emptyline(1)

    def indent(self, amount: int = 1) -> None:
        self.content += " " * amount

    def emptyline(self, amount: int = 1) -> None:
        self.content += "\n" * amount

    def dump(self) -> None:
        with open(self.filename, "a") as af:
            af.write(self.content.strip())

    def output(self) -> None:
        print(self.content.strip())
