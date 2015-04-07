# -*- coding: utf-8 -*-
{
    'name': 'Company Setup',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
     *  Install all required modules with company customizations.
     *  Insert company info and logo
    """,
    'author': 'netjunky.net',
    'website': 'www.netjunky.net',
    'depends': ['web','mail','crm','sale','stock','purchase','base_vat','website'],
    'init_xml': [],
    'data': [
        "views/res_company_view.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
