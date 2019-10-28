# -*- coding: utf-8 -*-
{
    'name': "l10n_mg_partner",

    'summary': """
        Extend partner informations""",

    'description': """
        Add VAT and another fiscal information on partner
    """,

    'author': "Frédéric Harison RAMANDANIARIVO",
    'website': "https://github.com/redykely/odoo_mg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale','account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/report_invoice_document_inherit_mg_partner.xml',
        'views/base_view_company_form_inherit_mg_partner.xml',
        'views/account_invoice_form_inherit_mg_partner.xml',
        'views/sale_view_order_form_inherit_mg_partner.xml',
    ],
    'demo': [],
    'auto_install': False,
    'installable': True,
}
