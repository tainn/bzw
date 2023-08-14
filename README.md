# bzw

[![black](https://img.shields.io/badge/style-black-222222.svg)](https://github.com/psf/black)
[![ruff](https://img.shields.io/badge/lint-ruff-222222.svg)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/type-mypy-222222.svg)](https://github.com/python/mypy)

A package that allows for simple [bzw](https://wiki.bzflag.org/BZW) object creation and file population.

It features no hard restrictions, meaning that any object can be created with any attribute, even if the object itself
does not exist. As such this package is merely an extension to creating maps by hand, making it more compact, better
organized, and allowing the inclusion of logic while building bzw objects.

### Install

Fetch the latest version of the package:

```console
python3 -m pip install --upgrade git+https://github.com/tainn/bzw.git
```

### Quick reference

A hands-on reference of available methods and their usability.

```py
import bzw

# Instantiation :: Bzw, LazyBzw
world = bzw.Bzw("my-map")

# Object creation :: create
world.create(
    "meshbox",
    position=(0, 0, 20),
    rotation=45,
    size=(10, 10, 10),
    color=(0.2, 0.2, 0.2, 0.9)
)

# Group definitions :: define
world.define("tower")
world.create("...")
world.define(end=True)

# Include :: include
world.include("/path/to/file.bzw")

# Empty lines :: emptyline
world.emptyline(2)

# Comments :: comment
world.comment("This is a comment")
world.comment("Two new lines afterwards", addline=True)

```

### Eager vs lazy

`Bzw` class provides an eager loading approach towards file population, with each bzw object being written into the end
file as you go. This omits the need to dump the incremental build at the end, as well as persists the built progress in
case of a runtime error. The trade-off is slightly worse performance due to repeating IO operations.

`LazyBzw` functions similarly to `Bzw`, but with lazy loading instead of eager loading. Additionally, it requires a
dump of the in-memory string content to perform a single write operation, usually at the very end.

```py
import bzw

# Eager
world = bzw.Bzw("my-map")

# Lazy
world = bzw.LazyBzw("my-map")
world.dump()
```

### Reserved keywords

When creating objects whose fields are named the same as
Python's [reserved keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords), we can add a trailing
underscore to the passed kwarg, which is then appropriately parsed during runtime.

In the example below, the `from_` kwarg is transformed into the `from` field, omitting the underscore. Note that all
leading and trailing underscores will be ignored in a similar fashion.

```py
world.create(
    "link",
    from_="east:f",
    to="west:b"
)
```

### Logic

By utilizing some form of logic, one line doesn't have to equal just one object creation. The following example creates
nine different objects under some key.

```py
for i in range(-4, 5):
    world.create(
        "meshbox",
        position=(i * 40, i * 40, 0),
        rotation=i * 10,
        size=(10, 10, 10 * abs(i) + 10)
    )
```
