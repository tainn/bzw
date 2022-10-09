# bzw

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A package written in Python that allows for simple bzw object creation and file population.

It features no hard restrictions, meaning that any object can be created with any attribute, even if the object itself
does not exist. As such this package is merely an extension to creating maps by hand, making it more compact, better
organized, and allowing the inclusion of logic while building bzw objects.

## Install

Fetch the latest version of the package

```sh
pip3 install --upgrade git+https://github.com/tainn/bzw.git
```

## Bzw

Eager loading approach towards file population, with each bzw object being written into the end file as you go. This
omits the need to dump the incremental build at the end, as well as persists the built progress in case of a runtime
error. The trade-off is slightly worse performance due to repeating IO operations.

### Import

Import the `bzw` module.

```py
import bzw
```

### Instantiation

Create a new object via the `Bzw` class. The constructor takes the following parameters:

- `filename` (required): desired bzw filename
- `overwrite` (optional): if set to `True`, overwrite bzw files with the same name

```py
world = bzw.Bzw("my-map", overwrite=False)
```

### Object creation

The core of creation is the `create` method. Pass in the type of the object, followed by key-value pairs for the value
fields. The values can be passed as strings, lists or tuples. If creating a group instance, the `group` parameter has to
be passed as `True`.

```py
world.create(
    "meshbox",
    position=(0, 0, 20),
    rotation=45,
    size=(10, 10, 10),
    color=(0.2, 0.2, 0.2, 0.9)
)

world.create(
    "tower",
    shift=(-20, -20, 30),
    drivethrough=1,
    group=True
)
```

### Group definitions

Groups can be defined and definitions closed via the `define` method. The method only has two forms: the definition
which takes a string name, as well as the definition closure which requires the `end` kwarg switch being set to `True`.

```py
world.define("tower")
# ... some object creations...
world.define(end=True)
```

### Include

External bzw files can be included via the `include` method.

```py
world.include("/path/to/file.bzw")
```

### Empty lines

In case we want to make the end bzw file more presentable and humanly readable, it is viable to insert empty lines in
between meaningful units. The `emptyline` method allows us to do so, accepting the number of empty lines to create and
defaulting to 1.

```py
world.emptyline(2)
```

### Comments

Like with the empty lines, comments via the `comment` method allow us to annotate our bzw file with humanly readable
text or other content that is later ignored during world generation. If an optional `addline` kwarg is passed as `True`,
an additional line is created at the end. For more new lines than that, combine this with the above `emptyline` method.

```py
world.comment("This is a comment...")
world.comment("... this one has two new lines afterwards", addline=True)
```

## LazyBzw

Functions similarly to the [Bzw](#Bzw) class, but with lazy loading instead of eager loading. Additionally, requires the
dump of the in-memory string content to perform a single write IO operation, usually at the very end.

```py
world.dump()
```

## Misc

### Reserved keywords

When creating objects whose fields are named the same as
Python's [reserved keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords), we can add a trailing
underscore to the passed kwarg, which is then appropriately parsed during runtime.

In the example below, the `from_` kwarg is transformed into the `from` field, omitting the underscore. Note that all
leading and trailing underscores will be ignored in a similar fashion.

```py
world.create("link", from_="east:f", to="west:b")
```

### Logic

By utilizing some form of logic, one line doesn't have to equal just one object creation. The below example creates nine
different objects under some key.

```py
for i in range(-4, 5):
    world.create(
        "meshbox",
        position=(i * 40, i * 40, 0),
        rotation=i * 10,
        size=(10, 10, 10 * abs(i) + 10)
    )
```
