# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Asset Management Retirement by Missing with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "fixed_asset_operating_unit",
        "fixed_asset_retirement_by_missing"
    ],
    "data": [
        "security/account_asset_retirement_by_missing_security.xml"
    ],
    "installable": True,
    "auto_install": True
}
