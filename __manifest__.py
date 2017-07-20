# -*- coding: utf-8 -*-
{
    'name': "Baja Agung",

    'summary': """
        Aplikasi Baja Agung""",

    'description': """
        Aplikasi Baja Agung
    """,

    'author': "Butirpadi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale', 'account', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/bja_sale_view.xml',
        'views/bja_partner_view.xml',
        'views/bja_salesperson_view.xml',
        'views/bja_product_views.xml',
        'views/bja_product_template_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True
    
}