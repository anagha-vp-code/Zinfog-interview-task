from odoo import models, fields, api


class SalesOrderField(models.Model):
    _inherit = 'sale.order.line'

    brand_name = fields.Char(string="Brand Name", related='product_id.brand_name', tracking=True)
    # min_cost = fields.Float(string="Minimum Cost")



