{
    'name': 'Stock Transport',
    'version': '1.0.0',
    'summary': 'Stock Transport',
    'description': "",
    'license': 'LGPL-3',
    'author': 'Lakshay Roopchandani',
    'depends': [
        'base',
        'stock_picking_batch',
        'fleet',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_move_views.xml'
    ],
    'installable': True,
}
