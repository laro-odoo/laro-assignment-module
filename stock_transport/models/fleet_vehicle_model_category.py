from odoo import fields, models, api

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float('Max Weight (Kg)')
    max_volume = fields.Float('Max Volume (m3)')

    @api.depends("name")
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.name:
                name = f"{name} ({record.max_weight}kg, {record.max_volume}m\N{SUPERSCRIPT THREE})"
            record.display_name = name
