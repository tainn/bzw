import bzw.utils as utils


class LazyBzw:
    def __init__(self, filename: str, overwrite: bool = False) -> None:
        self.filename: str = utils.set_filename(filename=filename, overwrite=overwrite)
        self.content: str = ""

    def create(self, typ: str, group: bool = False, **kwargs) -> None:
        if not group:
            self.content += f"{typ}\n"
        else:
            self.content += f"group {typ}\n"

        for attr in kwargs:
            # Non-array (fixed depth 0)
            if isinstance(kwargs[attr], (str, int, float)):
                self.content += f"{attr.strip('_')} {kwargs[attr]}\n"

            # Array of non-arrays (fixed depth 1)
            elif not any(isinstance(entry, (list, tuple, dict)) for entry in kwargs[attr]):
                kwargs[attr]: str = utils.deep_type_cast(core=kwargs, part=attr, name=attr)
                self.content += f"{attr.strip('_')} {kwargs[attr]}\n"

            # Array of arrays (max depth 2)
            else:
                for idx, _ in enumerate(kwargs[attr]):
                    partial: str = utils.deep_type_cast(core=kwargs[attr], part=idx, name=attr)
                    self.content += f"{attr.strip('_')} {partial}\n"

        self.content += "end\n\n"

    def define(self, name: str = None, end: bool = False) -> None:
        if not end:
            self.content += f"define {name}\n\n"
        else:
            self.content += "enddef\n\n"

    def include(self, path: str) -> None:
        self.content += f"include {path}\n\n"

    def emptyline(self, amount: int = 1) -> None:
        self.content += "\n" * amount

    def comment(self, content: str, addline: bool = False) -> None:
        if not addline:
            self.content += f"# {content}\n"
        else:
            self.content += f"# {content}\n\n"

    def dump(self):
        with open(self.filename, "a") as af:
            af.write(self.content)
