# bzw

[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/type-mypy-222a3d.svg)](https://github.com/python/mypy)

A package that allows for simple [bzw](https://wiki.bzflag.org/BZW) object creation and file population.

It features no hard restrictions, meaning that any object can be created with any attribute, even if the object itself
does not exist. As such this package is merely an extension to creating maps by hand, making it more compact, better
organized, and allowing the inclusion of logic while building bzw objects.

## Install

Fetch the latest version of the package:

```console
python3 -m pip install git+https://github.com/tainn/bzw.git@0.3.1
```

## Quick reference

A hands-on reference of available methods and their usability.

```py
from bzw import Bzw

# Instantiate
world = Bzw("my-map")

# Create objects
world.create(
    "meshbox",
    position=(0, 0, 20),
    rotation=45,
    size=(10, 10, 10),
    color=(0.2, 0.2, 0.2, 0.9),
)

# Define groups
world.define("tower")
world.create(...)
world.define(end=True)

# Include files
world.include("/path/to/file.bzw")

# Add comments
world.comment("This is a comment")

# Indent with spaces
world.indent(2)

# Add empty lines
world.emptyline(2)

# Dump to file
world.dump()

# Output to stdout
world.output()
```

## Dump and output

Since [`v3.0`](https://github.com/tainn/bzw/tree/v3.0), only the lazy IO approach is supported, in order to ensure a
complete end state in case of runtime errors.

This means that the final call of the `dump` method is required to write the in-memory string content to the end file.
The `output` method can also be called to print the creation to stdout instead of writing it to a file.

```py
from bzw import Bzw

world = Bzw("my-map")

...

world.output()
world.dump()
```

## Reserved keywords

When creating objects whose fields are named the same as
Python's [reserved keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords), we can add a trailing
underscore to the passed kwarg, which is then appropriately parsed during runtime.

In the example below, the `from_` kwarg is transformed into the `from` field, omitting the underscore. Note that all
leading and trailing underscores will be ignored in a similar fashion.

```py
world.create(
    "link",
    from_="east:f",
    to="west:b",
)
```

## Logic

By utilizing some form of logic, one line doesn't have to equal just one object creation. The following example creates
nine different objects under some key.

```py
for i in range(-4, 5):
    world.create(
        "meshbox",
        position=(i * 40, i * 40, 0),
        rotation=i * 10,
        size=(10, 10, 10 * abs(i) + 10),
    )
```
