# -*- coding: utf-8 -*-
{
    'name': "renala",

    'summary': """
        Modèle de Facture""",

    'description': """
        Modèle de facture customisée
        Doit être installée après l10n_mg_partner
    """,

    'author': "Ingenosya Madagascar",
    'website': "http://www.ingenosya.mg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_mg_partner','account'],

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