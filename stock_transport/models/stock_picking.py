from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    volume = fields.Float('Volume', compute='_compute_vol')

    @api.depends('move_ids.product_id.volume', 'move_ids.quantity')
    def _compute_vol(self):
        for record in self:
            for product in record.move_ids:
                record.volume += product.product_id.volume * product.quantity
