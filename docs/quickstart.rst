Quickstart
==========


Use debinix on the command line:

::

    $ debinix
    Hello world!

Show help:

::

    $ debinix --help
    usage: debinix [-h] [-V] [-c, --cowboy]
    
    optional arguments:
        -h, --help     show this help message and exit
        -V,            show the version and exit
        -c, --cowboy   cowboy greeting


Use debinix as a library:

::

    $ python3
    >>> from debinix.api.greetings import Greetings
    >>> print(Greetings())
    Hello world!
