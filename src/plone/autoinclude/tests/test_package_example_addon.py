from plone.autoinclude.tests.package_base import PackageTestCase

import unittest


class TestPackage(unittest.TestCase, PackageTestCase):
    project_name = "example.addon"
    features = ["addon"]
