# bzw

[BZW](https://wiki.bzflag.org/BZW) object creation and file population

## Install

Fetch the package via [uv](https://docs.astral.sh/uv)

```sh
uv pip install git+https://github.com/tainn/bzw.git@0.3.3
```

## Reference

A hands-on reference of available methods and their usability

```py
from bzw import Bzw

# instantiate
world = Bzw("my-map")

# create objects
world.create(
    "meshbox",
    position=(0, 0, 20),
    rotation=45,
    size=(10, 10, 10),
    color=(0.2, 0.2, 0.2, 0.9),
)

# define groups
world.define("tower")
world.create(...)
world.define(end=True)

# include files
world.include("/path/to/file.bzw")

# add comments
world.comment("this is a comment")

# indent with spaces
world.indent(2)

# add empty lines
world.emptyline(2)

# dump to file
world.dump()

# output to stdout
world.output()
```

## Dump and output

- A final call of the `dump()` method is required to write the in-memory string content to the end file
- The `output()` method can also be called to print the creation to stdout instead of writing it to a file

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
underscore to the passed kwarg, which is then appropriately parsed during runtime

In the example below, the `from_` kwarg is transformed into the `from` field, omitting the underscore. Note that all
leading and trailing underscores will be ignored in a similar fashion

```py
world.create(
    "link",
    from_="east:f",
    to="west:b",
)
```

## Logic

By utilizing some form of logic, one line doesn't have to equal just one object creation. The following example creates
nine different objects under some key

```py
for idx in range(-4, 5):
    world.create(
        "meshbox",
        position=(idx * 40, idx * 40, 0),
        rotation=idx * 10,
        size=(10, 10, 10 * abs(idx) + 10),
    )
```
