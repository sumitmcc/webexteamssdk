# -*- coding: utf-8 -*-
"""Model Webex Teams JSON objects as native Python objects.

Classes:
    SparkData: Models Spark JSON objects as native Python objects.

The SparkData class models any JSON object passed to it as a string or Python
dictionary as a native Python object; providing attribute access using native
dot-syntax (`object.attribute`).

Copyright (c) 2016-2018 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *
import json

from ..utils import json_dict


class SparkData(object):
    """Model a Spark JSON object as a native Python object."""

    def __init__(self, json_data):
        """Init a new SparkData object from a dictionary or JSON string.

        Args:
            json_data(dict, basestring): Input JSON string or dictionary.

        Raises:
            TypeError: If the input object is not a dictionary or string.

        """
        super(SparkData, self).__init__()
        self._json_data = json_dict(json_data)

    def __getattr__(self, item):
        """Provide native attribute access to the JSON object attributes.

        This method is called when attempting to access a object attribute that
        hasn't been defined for the object.  For example trying to access
        object.attribute1 when attribute1 hasn't been defined.

        SparkData.__getattr__() checks the original JSON object to see if the
        attribute exists, and if it does, it returns the attribute's value
        from the original JSON object.  This provides native access to all of
        the JSON object's attributes.

        Args:
            item(str): Name of the Attribute being accessed.

        Raises:
            AttributeError:  If the JSON object does not contain the attribute
                requested.

        """
        if item in list(self._json_data.keys()):
            item_data = self._json_data[item]
            if isinstance(item_data, dict):
                return SparkData(item_data)
            else:
                return item_data
        else:
            raise AttributeError(
                "'{}' object has no attribute '{}'"
                "".format(self.__class__.__name__, item)
            )

    def __str__(self):
        """A human-readable string representation of this object."""
        class_str = self.__class__.__name__
        json_str = json.dumps(self._json_data, indent=2)
        return "{}:\n{}".format(class_str, json_str)

    def __repr__(self):
        """A string representing this object as valid Python expression."""
        class_str = self.__class__.__name__
        json_str = json.dumps(self._json_data, ensure_ascii=False)
        return "{}({})".format(class_str, repr(json_str))

    @property
    def json_data(self):
        """A copy of the Spark data object's JSON data (OrderedDict)."""
        return self._json_data.copy()

    def to_dict(self):
        """Convert the Spark data to a dictionary."""
        return dict(self._json_data)

    def to_json(self, **kwargs):
        """Convert the Spark data to JSON.

        Any keyword arguments provided are passed through the Python JSON
        encoder.

        """
        return json.dumps(self._json_data, **kwargs)
