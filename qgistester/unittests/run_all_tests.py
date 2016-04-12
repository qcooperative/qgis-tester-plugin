# -*- coding: utf-8 -*-
"""Run all unit tests."""
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
import unittest
import sys
from qgistester.unittests.test_plugin import suite as pluginTestsSuite
from qgistester.unittests.test_report import suite as reportTestsSuite
from qgistester.unittests.test_ReportDialog import suite as \
                                           reportDialogTestsSuite
from qgistester.unittests.test_Test import suite as testTestsSuite
from qgistester.unittests.test_TesterWidget import suite as \
                                           testerWidgetTestsSuite
from qgistester.unittests.test_TestSelector import suite as \
                                           selectorTestsSuite
from qgistester.unittests.test_translations import suite as \
                                           translationsTestsSuite

# Tests for the QGIS Tester plugin. To know more see
# https://github.com/boundlessgeo/qgis-tester-plugin


def unitTests():
    """return array of test suites."""
    _tests = []
    _tests.extend(pluginTestsSuite())
    _tests.extend(reportTestsSuite())
    _tests.extend(reportDialogTestsSuite())
    _tests.extend(testTestsSuite())
    _tests.extend(testerWidgetTestsSuite())
    _tests.extend(selectorTestsSuite())
    _tests.extend(translationsTestsSuite())
    return _tests


def runAllUnitTests():
    """run all unittests."""
    _suite = unittest.TestSuite()
    _suite.addTest(pluginTestsSuite())
    _suite.addTest(reportTestsSuite())
    _suite.addTest(reportDialogTestsSuite())
    _suite.addTest(testTestsSuite())
    _suite.addTest(testerWidgetTestsSuite())
    _suite.addTest(selectorTestsSuite())
    _suite.addTest(translationsTestsSuite())
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(_suite)