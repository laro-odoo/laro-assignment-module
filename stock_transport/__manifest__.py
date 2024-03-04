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
        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
        'views/res_config_settings.xml',
    ],
    # 'demo': [

    # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
