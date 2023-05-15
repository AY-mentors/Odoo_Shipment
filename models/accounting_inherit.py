from odoo import fields, models, api


class AccountingBill(models.Model):
    _inherit = 'account.move'
    # _description = 'Description'

    Shipments_bill = fields.Many2one('shipment.data', string='Shipments', required=False)


class AccountingPayment(models.Model):
    # _name = 'account.payment'
    _inherit = 'account.payment'

    Shipments_payment = fields.Many2one('shipment.data', string='Shipments', required=False)
