import datetime
from datetime import datetime, timedelta

from odoo import fields, models, api, _


class DateNotification(models.Model):
    _name = 'date.notification'
    _rec_name = 'received_date_original_doc'
    _description = 'Date Notification'

    # shipment_id = fields.Integer(string='Shipment ID', required=False)
    shipment_name = fields.Char(string='Shipment name', required=False, readonly=True)
    received_date_original_doc = fields.Integer(string='تاريخ استلام النصر للمستندات الاصليه', required=False)
    send_date_bank_doc = fields.Integer(string='تاريخ ارسال المستندات الاصليه الي البنك', required=False)
    received_date_bank_doc = fields.Integer(string='تاريخ استلام المستندات من البنك', required=False)
    send_date_customs_broker = fields.Integer(string='تاريخ ارسال المستندات الي المخلص', required=False)
    tell_date_customs_broker = fields.Integer(string='تاريخ ابلاغ المخلص القيم الجمركية', required=False)
    issuance_date_cheque = fields.Integer(string='تاريخ اصدار الحسابات للشيكات الجمركية', required=False)
    release_date_shipment = fields.Integer(string='تاريخ الافراج عن الشحنه', required=False)
    appointment_date = fields.Integer(string='تاريخ التعيين', required=False)
    permission_date_shipment = fields.Integer(string='تاريخ استلام اذن استلام المخزن للشحنه', required=False)
    loading_date = fields.Integer(string='Loading Date', required=False)
    cut_off_date = fields.Integer(string='Cut Off Date', required=False)
    etd = fields.Integer(string='ETD', required=False)
    eta = fields.Integer(string='ETA', required=False)
    estimated_delivery = fields.Integer(string='Estimated Delivery', required=False)
    po_date = fields.Integer(string='Po Date', required=False)
    pi_date = fields.Integer(string='Pi Date', required=False)
    inv_date = fields.Integer(string='Inv Date', required=False)
    value_date = fields.Integer(string='Value Date', required=False)

    # @api.one
    @api.constrains('received_date_original_doc', 'send_date_bank_doc', 'received_date_bank_doc', 'send_date_customs_broker'
        , 'tell_date_customs_broker', 'issuance_date_cheque', 'release_date_shipment', 'appointment_date',
                    'permission_date_shipment'
        , 'loading_date', 'cut_off_date', 'etd', 'eta', 'estimated_delivery', 'po_date', 'pi_date', 'inv_date', 'value_date')
    def check_validation(self):

        for rec in self:
            v1 = str(rec.received_date_original_doc)
            d1 = v1[0]

            v2 = str(rec.send_date_bank_doc)
            d2 = v2[0]

            v3 = str(rec.received_date_bank_doc)
            d3 = v3[0]

            v4 = str(rec.send_date_customs_broker)
            d4 = v4[0]

            v5 = str(rec.tell_date_customs_broker)
            d5 = v5[0]

            v6 = str(rec.issuance_date_cheque)
            d6 = v6[0]

            v7 = str(rec.release_date_shipment)
            d7 = v7[0]

            v8 = str(rec.appointment_date)
            d8 = v8[0]

            v9 = str(rec.permission_date_shipment)
            d9 = v9[0]

            v10 = str(rec.loading_date)
            d10 = v10[0]

            v11 = str(rec.cut_off_date)
            d11 = v11[0]

            v12 = str(rec.etd)
            d12 = v12[0]

            v13 = str(rec.eta)
            d13 = v13[0]

            v14 = str(rec.estimated_delivery)
            d14 = v14[0]

            v15 = str(rec.po_date)
            d15 = v15[0]

            v16 = str(rec.pi_date)
            d16 = v16[0]

            v17 = str(rec.inv_date)
            d17 = v17[0]

            v18 = str(rec.value_date)
            d18 = v18[0]

            if d1 == '-' or d2 == '-' or d3 == '-' or d4 == '-' or d5 == '-' or d6 == '-' or d7 == '-' or d8 == '-' or d9 == '-' or d10 == '-' or d11 == '-' or d12 == '-' or d13 == '-' or d14 == '-' or d15 == '-' or d16 == '-' or d17 == '-' or d18 == '-':
                raise Warning(_('Values should not be -1.'))
