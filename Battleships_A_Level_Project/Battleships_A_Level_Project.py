"""

                            DOCUMENTATION STANDARDS
                            https://realpython.com/documenting-python-code/

Package and Module Docstrings
Package docstrings should be placed at the top of the package’s __init__.py file. 
This docstring should list the modules and sub-packages that are exported by the package.

Module docstrings are similar to class docstrings. 
Instead of classes and class methods being documented, it’s now the module and any functions found within. 
Module docstrings are placed at the top of the file even before any imports. 
Module docstrings should include the following:

A brief description of the module and its purpose
A list of any classes, exception, functions, and any other objects exported by the module

The docstring for a module function should include the same items as a class method:

A brief description of what the function is and what it’s used for
Any arguments (both required and optional) that are passed including keyword arguments
Label any arguments that are considered optional
Any side effects that occur when executing the function
Any exceptions that are raised
Any restrictions on when the function can be called

"""

class Animal:
    """
        Class Docstrings
        Class Docstrings are created for the class itself, as well as any class methods. 
        The docstrings are placed immediately following the class or class method indented by one level:

        Class docstrings should contain the following information:

        A brief summary of its purpose and behavior
        Any public methods, along with a brief description
        Any class properties (attributes)
        Anything related to the interface for subclassers, if the class is intended to be subclassed
        The class constructor parameters should be documented within the __init__ class method docstring. Individual methods should be documented using their individual docstrings. Class method docstrings should contain the following:

        A brief description of what the method is and what it’s used for
        Any arguments (both required and optional) that are passed including keyword arguments
        Label any arguments that are considered optional or have a default value
        Any side effects that occur when executing the method
        Any exceptions that are raised
        Any restrictions on when the method can be called
        Let’s take a simple example of a data class that represents an Animal. This class will contain a few class properties, instance properties, a __init__, and a single instance method:

    """