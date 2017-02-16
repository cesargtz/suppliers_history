# -*- coding: utf-8 -*-
{
    'name': "suppliers_history",

    'description': """
          This module gives information about suppliers contracts
    """,

    'author': "Yecora",
    'website': "yecora.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'purchases',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/suppliers_history.xml',],
}
