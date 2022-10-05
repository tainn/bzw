import bzw.utils as utils


class Bzw:
    def __init__(self, filename: str, overwrite: bool = False) -> None:
        self.filename: str = utils.set_filename(filename=filename, overwrite=overwrite)

    def create(self, typ: str, group: bool = False, **kwargs) -> None:
        with open(self.filename, "a") as f:
            if not group:
                f.write(f"{typ}\n")
            else:
                f.write(f"group {typ}\n")

            for attr in kwargs:
                # Non-array (fixed depth 0)
                if isinstance(kwargs[attr], (str, int, float)):
                    f.write(f"{attr.strip('_')} {kwargs[attr]}\n")

                # Array of non-arrays (fixed depth 1)
                elif not any(isinstance(entry, (list, tuple, dict)) for entry in kwargs[attr]):
                    kwargs[attr]: str = utils.deep_type_cast(core=kwargs, part=attr, name=attr)
                    f.write(f"{attr.strip('_')} {kwargs[attr]}\n")

                # Array of arrays (max depth 2)
                else:
                    for idx, _ in enumerate(kwargs[attr]):
                        partial: str = utils.deep_type_cast(core=kwargs[attr], part=idx, name=attr)
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
