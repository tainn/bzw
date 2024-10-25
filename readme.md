# bzw

a package that allows for simple [bzw](https://wiki.bzflag.org/BZW) object creation and file population

it features no hard restrictions, meaning that any object can be created with any attribute, even if the object itself
does not exist. as such this package is merely an extension to creating maps by hand, making it more compact, better
organized, and allowing the inclusion of logic while building bzw objects

## install

fetch the latest version of the package:

```console
python3 -m pip install git+https://github.com/tainn/bzw.git@0.3.2
```

## quick reference

a hands-on reference of available methods and their usability:

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
world.comment("This is a comment")

# indent with spaces
world.indent(2)

# add empty lines
world.emptyline(2)

# dump to file
world.dump()

# output to stdout
world.output()
```

## dump and output

since [`v3.0`](https://github.com/tainn/bzw/tree/v3.0), only the lazy io approach is supported, in order to ensure a
complete end state in case of runtime errors

this means that the final call of the `dump` method is required to write the in-memory string content to the end file.
the `output` method can also be called to print the creation to stdout instead of writing it to a file

```py
from bzw import Bzw

world = Bzw("my-map")

...

world.output()
world.dump()
```

## reserved keywords

when creating objects whose fields are named the same as
python's [reserved keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords), we can add a trailing
underscore to the passed kwarg, which is then appropriately parsed during runtime

in the example below, the `from_` kwarg is transformed into the `from` field, omitting the underscore. note that all
leading and trailing underscores will be ignored in a similar fashion

```py
world.create(
    "link",
    from_="east:f",
    to="west:b",
)
```

## logic

by utilizing some form of logic, one line doesn't have to equal just one object creation. the following example creates
nine different objects under some key:

```py
for i in range(-4, 5):
    world.create(
        "meshbox",
        position=(i * 40, i * 40, 0),
        rotation=i * 10,
        size=(10, 10, 10 * abs(i) + 10),
    )
```
