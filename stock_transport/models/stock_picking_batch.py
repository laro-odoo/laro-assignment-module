from odoo import fields, models, api

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('dock', 'Dock')
    vehicle = fields.Many2one('fleet.vehicle', 'Vehicle')
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', 'Vehicle Category')
    weight = fields.Float('Weight (Kg)', compute="_compute_param")
    volume = fields.Float('Volume (m3)', compute="_compute_param")
    weight_percentage = fields.Float('Weight (%)', default=0)
    volume_percentage = fields.Float('Volume (%)', default=0)

    @api.depends("weight", "volume")
    def _compute_param(self):
        for record in self:
            for product in record.move_line_ids:
                record.weight += product.product_id.weight * product.quantity
                record.volume += product.product_id.volume * product.quantity

            record.weight_percentage = (100 * record.weight ) / record.vehicle_category.max_weight if record.vehicle_category.max_weight > 0 else 0
            record.volume_percentage = 100 * record.volume / record.vehicle_category.max_volume if record.vehicle_category.max_volume > 0 else 0
