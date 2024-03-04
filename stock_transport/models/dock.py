from odoo import fields, models

class Dock(models.Model):
    _name = 'dock'

    name = fields.Char(string='Name')