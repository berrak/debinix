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

import unittest

from debinix.api.greetings import Greetings
from debinix.api.greetings import howdy_greeting


class TestApiGreetings(unittest.TestCase):
    """
    Test API classes and functions.

    """

    def test_api_greetings(self):
        msg = str(Greetings())
        self.assertEqual(msg, "Hello world!")

    def test_api_greetings_again(self):
        msg = str(Greetings("Hello again!"))
        self.assertEqual(msg, "Hello again!")

    def test_api_howdy(self):
        self.assertEqual(howdy_greeting(), "Howdy cowboy!")
