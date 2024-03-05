{
    'name': 'Stock Transport Settings',
    'version': '1.0.0',
    # 'category': 'Real Estate/Brokerage',
    'summary': 'Stock Transport Settings',
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
        'views/res_config_settings.xml',
    ],
    # 'demo': [

    # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
