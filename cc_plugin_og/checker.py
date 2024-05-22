import re

from compliance_checker import __version__
from compliance_checker.base import BaseCheck, Result
from compliance_checker.runner import ComplianceChecker, CheckSuite

from cc_plugin_og import OGChecker

class OGChecker(OGChecker):

    _cc_spec_version = "1.0"
    _cc_description = f"og {_cc_spec_version} compliance-checker"
    _cc_display_headers = {3: "Mandatory", 2: "Highly Recommended", 1: "Suggested"}

    METHODS_REGEX = re.compile(r"(\w+: *\w+) \((\w+: *\w+)\) *")
    PADDING_TYPES = ["none", "low", "high", "both"]


    def __init__(self):
        pass

    def check_manditory_variables(self, ds):
        """
        Check check for manditory variables.
        """

        level = BaseCheck.HIGH
        score = 0
        out_of = 1
        messages = []
        desc = "This checks basic requirements."

        required_variables = [
            "LATITUDE_GPS",
            "LONGITUDE_GPS",
            "TIME_GPS",
            "LATITUDE",
            "LONGITUDE",
            "TIME",
            "TRAJECTORY",
            "PLATFORM_MODEL",
            "WMO_IDENTIFIER",
            "PLATFORM_SERIAL_NUMBER",
            "DEPLOYMENT_TIME",
            "DEPLOYMENT_LATITUDE",
            "DEPLOYMENT_LONGITUDE",
        ]

        out_of = len(required_variables)

        for variable in required_variables:
            test = variable in ds.variables
            score += int(test)
            if not test:
                messages.append(f"Variable {variable} is missing")

        return self.make_result(level, score, out_of, desc, messages)

