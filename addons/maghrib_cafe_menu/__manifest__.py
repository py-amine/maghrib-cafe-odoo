{
    'name': 'MAGHRIB Cafe Menu and Stock',
    'version': '20.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Dynamic cafe menu, stock availability, and headless JSON API for React frontend',
    'author': 'Mohamed Amine Dhaini',
    'depends': ['base'],
    'data': [
        'security/ir.access.csv',
        'views/cafe_menu_views.xml',
        'data/cafe_menu_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}