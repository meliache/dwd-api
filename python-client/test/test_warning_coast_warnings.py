"""
    Deutscher Wetterdienst: API

    Aktuelle Wetterdaten von allen Deutschen Wetterstationen  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dwd.model.warning_coast_warnings501000007 import (
    WarningCoastWarnings501000007,
)

from deutschland import dwd

globals()["WarningCoastWarnings501000007"] = WarningCoastWarnings501000007
from deutschland.dwd.model.warning_coast_warnings import WarningCoastWarnings


class TestWarningCoastWarnings(unittest.TestCase):
    """WarningCoastWarnings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWarningCoastWarnings(self):
        """Test WarningCoastWarnings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WarningCoastWarnings()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()