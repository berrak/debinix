#!/usr/bin/env python3
#
# Copyright Bertil Kronlund, 2017
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
debinix.cli
-----------------------------------

Entry for the `debinix` CLI.

"""

import sys
import argparse

from debinix import __version__

from debinix.utils.environment import python_version

from debinix.api.greetings import Greetings
from debinix.api.greetings import howdy_greeting


def main(argv=sys.argv):

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-V, --version", help="show the version and exit", action="version",
        version="%(prog)s: version {version} (Python {pyversion})".format(version=__version__, pyversion=python_version()))

    parser.add_argument(
        "-c, --cowboy", help="cowboy greeting",
        action="store_true", dest="iscowboy",
        default=False)

    args = parser.parse_args()

    # Do some meaningful ...
    if args.iscowboy:
        print(howdy_greeting())
    else:
        greetings = Greetings()
        print(greetings)

    return 0
