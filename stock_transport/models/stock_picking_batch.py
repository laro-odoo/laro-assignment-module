from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('dock', 'Dock')
    vehicle = fields.Many2one('fleet.vehicle', 'Vehicle')
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', 'Vehicle Category')
    weight = fields.Float('Weight (Kg)', compute="_compute_weight", store=True)
    volume = fields.Float('Volume (m3)', compute="_compute_volume", store=True)
    weight_percentage = fields.Float('Weight (%)', compute='_compute_weight_percent')
    volume_percentage = fields.Float('Volume (%)', compute='_compute_volume_percent')
    transfer = fields.Float(compute='_compute_transfer', store=True)
    lines = fields.Float(compute='_compute_lines', store=True)
    # move_ids1 = fields.One2many('stock.move', 'picking_batch_id', 'Moves')

    @api.depends('picking_ids')
    def _compute_transfer(self):
        for record in self:
            record.transfer = len(record.picking_ids)
    
    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
            record.lines = len(record.move_line_ids)
    
    
    @api.depends('picking_ids.move_ids.quantity', 'picking_ids.move_ids.product_id.weight')
    def _compute_weight(self):
        for record in self:
            record.weight = 0
            for order in record.picking_ids:
                for product in order.move_ids:
                    record.weight += product.product_id.weight * product.quantity

    @api.constrains('weight')
    def _check_weight(self):
        for record in self:
            if record.weight > record.vehicle_category.max_weight:
                raise ValidationError(_('check the weight'))


    @api.depends('weight')
    def _compute_weight_percent(self):
        for record in self:
            record.weight_percentage = (100 * record.weight) / record.vehicle_category.max_weight if record.vehicle_category.max_weight > 0 else 0
            
    @api.depends('picking_ids.move_ids.quantity', 'picking_ids.move_ids.product_id.volume')
    def _compute_volume(self):
        for record in self:
            record.volume = 0
            for order in record.picking_ids:
                for product in order.move_ids:
                    record.volume += product.product_id.volume * product.quantity
                    
    @api.depends('volume')
    def _compute_volume_percent(self):
        for record in self:
            record.volume_percentage = (100 * record.volume) / record.vehicle_category.max_volume if record.vehicle_category.max_volume > 0 else 0
    
    @api.depends("name")
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.name:
                name = name + ": " + str(round(record.weight, 2)) + "kg, " + str(round(record.volume, 2)) + "m\N{SUPERSCRIPT THREE}"
            record.display_name = name
