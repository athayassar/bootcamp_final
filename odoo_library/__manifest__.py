# -*- coding: utf-8 -*-
{
    'name': "odoo_library",

    'summary': "Modul Perpustakaan",

    'description': """
Modul Perpustakaan
    """,

    'author': "Alldi",
    'website': "https://www.bootcamp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'report/report_library_transaction.xml',
        # 'report/report_action.xml',
        'security/ir.model.access.csv',
        'views/training_views.xml',
        'views/menuitem_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

