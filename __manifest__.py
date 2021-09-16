# -*- coding: utf-8 -*-
{
    'name': "Gerenciador Alunos",

    'summary': """
        Cadastro e visualização dos alunos""",

    'description': """
        Cadastro e visualização dos alunos
    """,

    'author': "Netcom Treinamentos e Soluções Tecnológicas",
    'website': "http://www.netcom-ma.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Academico',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','l10n_br_base_address'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/alunos_view.xml',
        'views/res_partner_views.xml',
        'reports/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
