import os
from typing import Union


class Bzw:
    def __init__(self, filename: str, overwrite: bool = False) -> None:
        self.filename: str = _set_filename(filename=filename, overwrite=overwrite)

    def create(self, ref: str, group: bool = False, **kwargs) -> None:
        with open(self.filename, "a") as f:
            if not group:
                f.write(f"{ref}\n")
            else:
                f.write(f"group {ref}\n")

            for attr in kwargs:
                # Non-array
                if isinstance(kwargs[attr], (str, int, float)):
                    f.write(f"{attr.strip('_')} {kwargs[attr]}\n")

                # Array of non-arrays
                elif not any(isinstance(entry, (list, tuple, dict)) for entry in kwargs[attr]):
                    kwargs[attr]: str = _deep_type_cast(core=kwargs, part=attr, name=attr)
                    f.write(f"{attr.strip('_')} {kwargs[attr]}\n")

                # Array of arrays
                else:
                    for idx, _ in enumerate(kwargs[attr]):
                        partial: str = _deep_type_cast(core=kwargs[attr], part=idx, name=attr)
                        f.write(f"{attr.strip('_')} {partial}\n")

            f.write("end\n\n")

    def define(self, name: str = None, end: bool = False) -> None:
        with open(self.filename, "a") as f:
            if not end:
                f.write(f"define {name}\n\n")
            else:
                f.write("enddef\n\n")

    def include(self, path: str) -> None:
        with open(self.filename, "a") as f:
            f.write(f"include {path}\n\n")

    def emptyline(self, amount: int = 1) -> None:
        with open(self.filename, "a") as f:
            f.write("\n" * amount)

    def comment(self, content: str, addline: bool = False) -> None:
        with open(self.filename, "a") as f:
            if not addline:
                f.write(f"# {content}\n")
            else:
                f.write(f"# {content}\n\n")


def _set_filename(filename: str, overwrite: bool = False) -> str:
    init_name: str = filename if filename.endswith(".bzw") else f"{filename}.bzw"
    name: str = init_name
    postfix_incr: int = 1

    while True:
        if os.path.isfile(name) and not overwrite:
            name: str = f'{init_name.split(".bzw")[0]}-{str(postfix_incr).zfill(2)}.bzw'
            postfix_incr += 1
        elif os.path.isfile(name) and overwrite:
            os.remove(name)
            break
        else:
            break

    return name


def _deep_type_cast(core: Union[dict, list, tuple], part: Union[str, int], name: str) -> str:
    core[part]: str = _array_check_form(core=core, part=part)
    core[part]: str = _dict_check_form(core=core, part=part, name=name)
    return core[part]


def _array_check_form(core: Union[dict, list, tuple], part: Union[str, int]) -> str:
    if not isinstance(core[part], (list, tuple)):
        return core[part]

    return " ".join(map(str, core[part]))


def _dict_check_form(core: Union[dict, list, tuple], part: Union[str, int], name: str) -> str:
    if not isinstance(core[part], dict):
        return core[part]

    build: str = "\n"

    for key in core[part]:
        build += f"  {key.strip('_')} {_array_check_form(core=core[part], part=key)}\n"

    build += f"end{name}"
    return build
