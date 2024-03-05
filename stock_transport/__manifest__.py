{
    'name': 'Stock Transport',
    'version': '1.0.0',
    # 'category': 'Real Estate/Brokerage',
    'summary': 'Stock Transport',
    'description': "",
    'license': 'LGPL-3',
    'author': 'Lakshay Roopchandani',
    'depends': [
        'base',
        'stock_picking_batch',
        'fleet',
    ],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',

        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
    ],
    # 'demo': [

    # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
