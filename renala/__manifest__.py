# -*- coding: utf-8 -*-
{
    'name': "renala",

    'summary': """
        Personnalistion RENALA""",

    'description': """
        Modèle de facture customisée
        Doit être installée après l10n_mg_partner
    """,

    'author': "Ingenosya Madagascar",
    'website': "http://www.ingenosya.mg",

    'version': '0.1',

    'depends': ['base','l10n_mg_partner','account'],

    'data': [
        'views/res_partner.xml',
        'report/account_invoice.xml',
    ],
}