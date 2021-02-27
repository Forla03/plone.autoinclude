from plone.autoinclude.tests.integration_base import IntegrationTestCase

import unittest


class TestIntegration(IntegrationTestCase, unittest.TestCase):
    project_name = "example.ploneintegration"
    target = "plone"
    meta_files = {
        "example.ploneintegration": ["meta.zcml"],
        "plone.autoinclude": ["meta.zcml"],
        "example.metaoverrides": ["meta.zcml"],
        "example.somethingelse2": ["meta.zcml"],
    }
    configure_files = {
        "example.ploneintegration": ["configure.zcml"],
        "example.ploneaddon": [
            "configure.zcml",
            "permissions.zcml",
            "browser/configure.zcml",
        ],
        "example.somethingelse2": ["configure.zcml"],
        "example.multipleeps": ["configure.zcml"],
    }
    overrides_files = {
        "example.ploneintegration": ["overrides.zcml"],
        "example.metaoverrides": ["overrides.zcml"],
        "example.somethingelse2": ["overrides.zcml"],
    }
    features = [
        "different2",
        "disable-autoinclude",
        "metaoverrides",
        "ploneintegration",
    ]
