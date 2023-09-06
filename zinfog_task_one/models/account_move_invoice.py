from odoo import models, fields, api


class AccountMoveDelivery(models.Model):
    _inherit = 'account.move'

    delivery_charge_invoice = fields.Float(string="Delivery Charge", compute="_compute_delivery_charge")





