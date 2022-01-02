# bzw-wrapper

`bzwrap` is a package written in Python that allows for simple bzw object creation and file population.

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
import bzwrap

# Set a filename
bzw = bzwrap.Bzw('my_map', overwrite=False)

# Create objects
bzw.create('meshbox', position=(0, 0, 20), rotation=45, size=(10, 10, 10))
bzw.create('meshpyr', position=(-20, -20, 30), size=(5, 5, 20), color=(0.2, 0.2, 0.2, 0.9))

# Group definitions
bzw.define('tower')
# ...
bzw.define(end=True)

# Include
bzw.include('/path/to/file.bzw')

# Empty lines
bzw.emptyline(2)

# Comments
bzw.comment('This is a comment')
bzw.comment('This comment has two new lines afterwards', addline=True)
```

## Logic

By utilizing some form of logic, one line doesn't have to equal just one object creation.

```py
import bzwrap

bzw = bzwrap.Bzw('my_map')

# Creation of nine objects under some key
for i in range(-4, 5):
    bzw.create('meshbox', position=(i * 40, i * 40, 0), rotation=i * 10, size=(10, 10, 10 * abs(i) + 10))
```

## Output

The output of running such a script is a `my_map.bzw` file, created in the same directory as the executable, which
features the objects created during runtime.

If `overwrite=True` is passed during object creation and a file with that name already exists in the working directory,
the file is overwritten. Otherwise, a sequential number is appended, e.g. `my_map-02.bzw`, which is also the default
behavior.
