from odoo import models, fields, api


class SalesOrderInherit(models.Model):
    _inherit = 'product.product'

    brand_name = fields.Char(string="Brand Name")
    min_cost = fields.Float(string="Minimum Cost")



