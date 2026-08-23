{
    'name': 'FODEC & Timbre Fiscal',
    'version': '19.0.1.0.0',
    'summary': 'Add FODEC and Timbre Fiscal to customer invoices',
    'description': """
        Tunisian Invoice Compliance Module
        ==================================
        This module adds functionality to handle FODEC and Timbre Fiscal 
        on customer invoices according to Tunisian fiscal rules.
    """,
    'category': 'Accounting/Localizations',
    'author': 'Expert Odoo Developer',
    'depends': ['account'],
    'data': [
        'data/product_data.xml',
        'views/account_move_views.xml',
        'report/report_invoice_tn.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
