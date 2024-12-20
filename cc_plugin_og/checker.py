import re

from compliance_checker import __version__
from compliance_checker.base import BaseCheck
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

    def check_mandatory_variables(self, ds):
        """
        Check check for mandatory variables.
        """

        level = BaseCheck.HIGH
        score = 0
        messages = []
        desc = "Check for mandatory variables."

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


    def check_attribute_names_are_lowercase(self, ds):
        """
        Check that all attribute names are lowercase.
        """

        level = BaseCheck.HIGH
        score = 0
        out_of = 0
        messages = []
        desc = "Check that all attribute names are lowercase."

        # Check global attributes
        attr_exceptions = ["Conventions", "featureType"]
        for attr in ds.ncattrs():
            if attr in attr_exceptions:
                continue
            out_of += 1
            test = attr.lower()
            if test != attr:
                messages.append(f"Global attribute {attr} should be lowercase: {test}")
            else:
                score += 1

        # Check variable attributes
        # Skip [masked, masked_array] variable attributes
        attr_exceptions = ["_FillValue"]
        for variable in ds.variables:
            for attr in ds.variables[variable].ncattrs():
                if attr in attr_exceptions:
                    continue
                out_of += 1
                try:
                    test = attr.lower()
                except Exception as inst:
                    print("Exception: ", type(inst))
                    breakpoint()

                if test != attr:
                    messages.append(f"Variable {variable} attribute {attr} should be lowercase: {test}")
                else:
                    score += 1

        return self.make_result(level, score, out_of, desc, messages)


    def check_variable_names_are_capitalized(self, ds):
        """
        Check that variable names are capitalized.
        """

        level = BaseCheck.HIGH
        score = 0
        out_of = len(ds.variables)
        messages = []
        desc = "Variable names should be capitalized."

        for variable in ds.variables:
            test = variable.upper()
            if test != variable:
                messages.append(f"Variable {variable} should be capitalized: {test}")
            else:
                score += 1

        return self.make_result(level, score, out_of, desc, messages)

    def check_mandatory_global_attributes(self, ds):
        """
        Check for mandatory global attributes.
        """

        level = BaseCheck.HIGH
        score = 0
        messages = []
        desc = "Check for mandatory global attributes."

        required_attributes = [
            'title',
            'platform',
            'platform_vocabulary',
            'id',
            'contributor_name',
            'comment',
            'contributor_name',
            'contributor_email',
            'contributor_role',
            'contributor_role_vocabulary',
            'contributing_institutions',
            'contributing_institutions_role',
            'contributing_institutions_role_vocabulary',
            'rtqc_method',
            'start_date',
            'date_created',
            'featureType',
            'featureType',
            'Conventions',
        ]

        out_of = len(required_attributes)
        for attribute in required_attributes:
            test = attribute in ds.ncattrs()
            score += int(test)
            if not test:
                messages.append(f"Global attribute {attribute} is missing")

        return self.make_result(level, score, out_of, desc, messages)
    