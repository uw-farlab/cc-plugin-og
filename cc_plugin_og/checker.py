import re

from compliance_checker.base import BaseCheck

from cc_plugin_og import OGChecker

class OGChecker(OGChecker):
    _cc_spec_version = "1.0"
    _cc_description = f"OG {_cc_spec_version} compliance-checker"
    _cc_display_headers = {3: "Highly Recommended", 2: "Recommended", 1: "Suggested"}

    METHODS_REGEX = re.compile(r"(\w+: *\w+) \((\w+: *\w+)\) *")
    PADDING_TYPES = ["none", "low", "high", "both"]

    def __init__(self):
        pass

    def check_basic_requirements(self, dataset):
        """
        Check basic OG stated conventions.
         * Format follows the CF 1.8 convention.
         * Format follows the ACDD 1.3 convention.
         * Variables are identified in capital letters.
         * Attributes are identified in lower case.
        """

        level = BaseCheck.HIGH
        score = 0
        out_of = 1
        messages = []
        desc = "This checks variable and attribute conventions."

        # Do test things here
        ans = 0

        try:
            assert ans == 0
        except AssertionError:
            # Many messages may be appended here
            m = 'Variable and attribute convention test failed.'
            messages.append(m)
        else:
            score += 1

        return self.make_result(level, score, out_of, desc, messages)
