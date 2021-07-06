# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Asset Management Estimation Change with Operating Units",
    "version": "8.0.1.0.0",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "website": "https://opensynergy-indonesia.com",
    "category": "Accounting",
    "depends": [
        "fixed_asset_operating_unit",
        "fixed_asset_estimation_change"
    ],
    "data": [
        "security/account_asset_change_estimation_salvage_security.xml",
        "security/account_asset_change_estimation_useful_life_security.xml"
    ],
    "installable": True,
    "auto_install": True
}
