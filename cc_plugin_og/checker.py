import re
import datetime

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

    def check_dimensions(self, ds):
        """
        Check for mandatory dimensions
        """
        level = BaseCheck.HIGH
        score = 0
        messages = []
        desc = "Check for mandatory dimensions."
        required_dims = [
            'N_MEASUREMENTS',
        ]
        out_of = len(required_dims)

        for dimension in required_dims:
            test = dimension in ds.dimensions.keys()
            score += int(test)
            if not test:
                messages.append(f"Dimension {dimension} is missing")

        return self.make_result(level, score, out_of, desc, messages)

    def check_mandatory_variables(self, ds):
        """
        Check for mandatory variables.
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
            "DEPTH",
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

    def check_sensors(self, ds):
        """
        Check that all sensors referred to in variables are present.
        """

        level = BaseCheck.HIGH
        score = 0
        messages = []
        sensors = []
        desc = "sensors referred to in variables should be present"
        for variable in ds.variables:
            attrs = ds.variables[variable].ncattrs()
            if 'sensor' in attrs:
                sensors.append(ds.variables[variable].getncattr('sensor'))

        sensors = set(sensors)
        out_of = len(sensors)

        for sensor in sensors:
            test = sensor in ds.variables
            if not test:
                messages.append(f"Sensor variable {sensor} is missing")
            else:
                score += int(test)

        return self.make_result(level, score, out_of, desc, messages)


    def check_dates(self, ds):
        """
        Check that all dates in metadata are correctly formatted
        """
        level = BaseCheck.HIGH
        score = 0
        messages = []
        desc = "dates should be formatted as YYYYmmddTHHMMss"
        
        dates_to_check = ["start_date", "date_created", "time_coverage_start", "time_coverage_end"]
        attrs = ds.ncattrs()
        dates = set(dates_to_check).intersection(attrs)
        out_of = len(dates)

        for date_name in dates:
            date_str = ds.getncattr(date_name)
            try:
                datetime.datetime.strptime(date_str, "%Y%m%dT%H%M%S")
                score += 1
            except ValueError:
                messages.append(f"Date {date_name}: {date_str} is not formatted as YYYYmmddTHHMMss")

        return self.make_result(level, score, out_of, desc, messages)
