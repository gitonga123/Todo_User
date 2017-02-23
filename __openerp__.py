# -*- coding: utf-8 -*-
{
    'name': "Todo User",

    'summary': """
        Extend  the To-Do   app to  multiuser""",

    'description': """
        Extend  the To-Do   app to  multiuser
    """,

    'author': "Daniel Mutwiri",
    'website': "http://www.youtube.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','todo','mail',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}