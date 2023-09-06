from odoo import models, fields, api


class SalesOrderInherit(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Float(string="Delivery Charge", compute="_compute_delivery_charge")

    @api.depends('amount_total')

    def _compute_delivery_charge(self):
        for r in self:
            r.delivery_charge = r.amount_total*10/100
# add delivery charge into invoice
    def _prepare_invoice(self):
        invoice_vals = super(SalesOrderInherit, self)._prepare_invoice()
        invoice_vals['delivery_charge_invoice'] = self.delivery_charge
        print("invoice vals", invoice_vals)
        return invoice_vals

