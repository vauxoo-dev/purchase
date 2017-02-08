# -*- coding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: Nhomar Hernandez <nhomar@vauxoo.com>
#    planned by: Nhomar Hernandez <nhomar@vauxoo.com>
############################################################################

{
    "name": "Purchase Console",
    "summary": "Manage your purchase planning wasn't so simple ever.",
    "version": "10.0.0.0.2",
    "license": "AGPL-3",
    "author": "Vauxoo",
    "sequence": 100,
    "website": "http://www.vauxoo.com/",
    "category": "",
    "depends": [
        # PRODUCT HELPERS.
        # Conceptually the master product management starts here.
        "product_lifecycle",
        # necessary to use it as filter and analysis.
        "product_manufacturer",
        # Important tool to manage better the set of products
        "product_properties_by_category",
        # Proper cost management.
        "stock_landed_costs_segmentation",
        # Stock
        "purchase_rfq_xls",  # We need the original report in xls
        # To ensure a proper costing method configurable for all products.
        "costing_method_settings",
        # Technical tools.
        "message_post_model",  # Just because log properly some +2many
        # computation process here
        "forecasting_smoothing_techniques"
    ],
    "data": [
        'views/assets_backend.xml',
        'views/purchase_requisition_view.xml',
        'views/layout.xml',
        'wizard/fill_products_wizard_view.xml',
        'data/data.xml',
    ],
    "demo": [
    ],
    "test": [],
    "qweb": [
        'static/xml/console.xml',
        'static/xml/web_widget_one2many_console.xml',
    ],
    "js": [
    ],
    "installable": True,
    "application": True,
    'auto_install': False,
}
