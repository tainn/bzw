import bzw.utils as utils


class Bzw:
    def __init__(self, filename: str, overwrite: bool = False) -> None:
        self.filename: str = utils.set_filename(filename=filename, overwrite=overwrite)

    def create(self, typ: str, group: bool = False, **kwargs) -> None:
        with open(self.filename, "a") as af:
            if not group:
                af.write(f"{typ}\n")
            else:
                af.write(f"group {typ}\n")

            for attr in kwargs:
                if isinstance(kwargs[attr], (str, int, float)):
                    af.write(f"{attr.strip('_')} {kwargs[attr]}\n")

                elif not any(isinstance(entry, (list, tuple, dict)) for entry in kwargs[attr]):
                    kwargs[attr]: str = utils.deep_type_cast(core=kwargs, part=attr, name=attr)
                    af.write(f"{attr.strip('_')} {kwargs[attr]}\n")

                else:
                    for idx, _ in enumerate(kwargs[attr]):
                        partial: str = utils.deep_type_cast(core=kwargs[attr], part=idx, name=attr)
                        af.write(f"{attr.strip('_')} {partial}\n")

            af.write("end\n\n")

    def define(self, name: str = None, end: bool = False) -> None:
        with open(self.filename, "a") as af:
            if not end:
                af.write(f"define {name}\n\n")
            else:
                af.write("enddef\n\n")

    def include(self, path: str) -> None:
        with open(self.filename, "a") as af:
            af.write(f"include {path}\n\n")

    def emptyline(self, amount: int = 1) -> None:
        with open(self.filename, "a") as af:
            af.write("\n" * amount)

    def comment(self, content: str, addline: bool = False) -> None:
        with open(self.filename, "a") as af:
            if not addline:
                af.write(f"# {content}\n")
            else:
                af.write(f"# {content}\n\n")
