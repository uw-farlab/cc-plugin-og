import re

from compliance_checker.base import BaseCheck

from cc_plugin_og import OGChecker

class OGChecker(OGChecker):
    _cc_spec_version = "1.0"
    _cc_description = f"og {_cc_spec_version} compliance-checker"
    _cc_display_headers = {3: "Mandatory", 2: "Highly Recommended", 1: "Suggested"}

    METHODS_REGEX = re.compile(r"(\w+: *\w+) \((\w+: *\w+)\) *")
    PADDING_TYPES = ["none", "low", "high", "both"]

    def __init__(self):
        pass

    def check_mandatory_variables(self, dataset):
        """
        Check check_basic_requirements()
        """

        level = BaseCheck.HIGH
        score = 0
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
            try:
                assert variable in dataset.variables
            except AssertionError:
                score += 1
                messages.append(f"Variable {variable} is missing")

        return self.make_result(level, score, out_of, desc, messages)

    def check_advanced_requirements(self, dataset):
        """
        Check check_advanced_requirements()
        """

        level = BaseCheck.HIGH
        score = 0
        out_of = 1
        messages = []
        desc = "This checks advanced requirements."

        # Do test things here
        ans = 0

        try:
            assert ans == 0
        except AssertionError:
            # Many messages may be appended here
            m = '... test failed.'
            messages.append(m)
        else:
            score += 1

        return self.make_result(level, score, out_of, desc, messages)

    def check_basic_requirements5(self, dataset):
        """
        Check check_basic_requirements5()
        """

        level = BaseCheck.HIGH
        score = 0
        out_of = 1
        messages = []
        desc = "This checks basic requirements."

        # Do test things here
        ans = 0

        try:
            assert ans == 0
        except AssertionError:
            # Many messages may be appended here
            m = '... test failed.'
            messages.append(m)
        else:
            score += 1

        return self.make_result(level, score, out_of, desc, messages)

    def check_basic_requirements2(self, dataset):
        """
        Check check_basic_requirements2()
        """

        level = BaseCheck.HIGH
        score = 0
        out_of = 1
        messages = []
        desc = "This checks basic requirements."

        # Do test things here
        ans = 0

        try:
            assert ans == 0
        except AssertionError:
            # Many messages may be appended here
            m = '... test failed.'
            messages.append(m)
        else:
            score += 1

        return self.make_result(level, score, out_of, desc, messages)

    def check_basic_requirements7(self, dataset):
        """
        Check check_basic_requirements7()
        """

        level = BaseCheck.HIGH
        score = 0
        out_of = 1
        messages = []
        desc = "This checks basic requirements."

        # Do test things here
        ans = 0

        try:
            assert ans == 0
        except AssertionError:
            # Many messages may be appended here
            m = '... test failed.'
            messages.append(m)
        else:
            score += 1

        return self.make_result(level, score, out_of, desc, messages)

