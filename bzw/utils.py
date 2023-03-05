import os


def set_filename(filename: str, overwrite: bool = False) -> str:
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


def deep_type_cast(core: dict | list | tuple, part: str | int, name: str) -> str:
    core[part]: str = array_check_form(core=core, part=part)
    core[part]: str = dict_check_form(core=core, part=part, name=name)
    return core[part]


def array_check_form(core: dict | list | tuple, part: str | int) -> str:
    if not isinstance(core[part], (list, tuple)):
        return core[part]

    return " ".join(map(str, core[part]))


def dict_check_form(core: dict | list | tuple, part: str | int, name: str) -> str:
    if not isinstance(core[part], dict):
        return core[part]

    build: str = "\n"

    for key in core[part]:
        build += f"  {key.strip('_')} {array_check_form(core=core[part], part=key)}\n"

    build += f"end{name}"
    return build
