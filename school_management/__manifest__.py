# -*- coding: utf-8 -*-
{
    'name': "school management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': "However",

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base' , 'mail'],


    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/email_template.xml', # Add this line
        'data/scheduled_action.xml',  # Add this line
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True ,
}

