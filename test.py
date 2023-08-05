import unittest

from src.tests.test_page import TestPage


if __name__ == "__main__":
    suites = []
    for suite in [
        TestPage
    ]:
        suites.append(unittest.makeSuite(suite))

    testSuite = unittest.TestSuite(suites)
    testSuite.run()