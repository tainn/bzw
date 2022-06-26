# bzw-wrapper

![package_version](https://img.shields.io/badge/package-2.1-b0c9ff)
![python_version](https://img.shields.io/badge/python-3.6-b0c9ff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A package written in Python that allows for simple bzw object creation and file population.

It features no hard restrictions, meaning that any object can be created with any attribute, even if the object itself
does not exist. As such this package is merely an extension to creating maps by hand, making it more compact, better
organized, and allowing the inclusion of logic while building bzw objects.

## Install

Fetch the latest version of the package

```sh
pip3 install --user --upgrade git+git://github.com/tainn/bzw-wrapper.git
```

## Usage

```py
import bzw

# Set a filename
world = bzw.Bzw('my_map', overwrite=False)

# Create objects
world.create('meshbox', position=(0, 0, 20), rotation=45, size=(10, 10, 10))
world.create('meshpyr', position=(-20, -20, 30), size=(5, 5, 20), color=(0.2, 0.2, 0.2, 0.9))

# Group definitions
world.define('tower')
# ... some object creations...
world.define(end=True)

# Include
world.include('/path/to/file.bzw')

# Empty lines
world.emptyline(2)

# Comments
world.comment('This is a comment...')
world.comment('... this one has two new lines afterwards', addline=True)
```

### Overwrite

The output of running such a script is a `my_map.bzw` file, created in the same directory as the executable, which
features the objects created during runtime.

If `overwrite=True` is passed during object creation and a file with that name already exists in the working directory,
the file is overwritten. Otherwise, a sequential number is appended, e.g. `my_map-02.bzw`, which is also the default
behavior.

### Reserved keywords

When creating objects whose fields are named the same as
Python's [reserved keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords), we can add a trailing
underscore to the passed kwarg, which is then appropriately parsed during runtime.

```py
world.create('link', from_='east:f', to='west:b')
```

In the example above, the `from_` kwarg is transformed into the `from` field, omitting the underscore. Note that all
leading and trailing underscores will be ignored in a similar fashion.

## Logic

By utilizing some form of logic, one line doesn't have to equal just one object creation.

```py
import bzw

world = bzw.Bzw('my_map')

# Creation of nine objects under some key
for i in range(-4, 5):
    world.create(
        'meshbox',
        position=(i * 40, i * 40, 0),
        rotation=i * 10,
        size=(10, 10, 10 * abs(i) + 10)
    )
```
