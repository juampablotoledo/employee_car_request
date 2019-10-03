# -*- coding: utf-8 -*-
{
    'name': "Employee Car Request",

    'summary': """
       Request a car and get the approval""",

    'description': """
        Manage the needs of cars in your company """,

    'author': "Juan Pablo Toledo",
    'website': "https://github.com/juampablotoledo/employee_car_request.git",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet', 'hr'],

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