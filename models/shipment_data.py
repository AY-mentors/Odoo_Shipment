import datetime
from datetime import datetime, timedelta

from odoo import fields, models, api, _


class ShipmentData(models.Model):
    _name = 'shipment.data'
    _rec_name = 'seq_no'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Shipment Date'

    # Will Exchange it by generate automation
    rec_id_save = fields.Integer(string='Record ID')
    seq_no = fields.Char(string='Serial.NO')
    suppliers = fields.Many2one('res.partner', string='Suppliers', required=False)
    consignee = fields.Char(string='Consignee', required=False)
    sap = fields.Integer(string='Sap', required=False)
    po = fields.Many2one('purchase.order', string='Po', required=False)
    po_date = fields.Datetime(string='Po Date', required=False)
    po_amount = fields.Integer(string='Po amount', required=False)
    pi = fields.Integer(string='Pi', required=False)
    pi_date = fields.Datetime(string='Pi date', required=False)
    pi_amount = fields.Integer(string='Pi amount', required=False)
    final_inv_no = fields.Integer(string='Final inv no', required=False)
    inv_date = fields.Datetime(string='Inv date', required=False)
    inv_amount = fields.Integer(string='Inv amount', required=False)
    bank_transfer_amount = fields.Integer(string='Bank transfer amount', required=False)
    value_date = fields.Datetime(string='Value date', required=False)
    bank_name_branch = fields.Char(string='Bank name branch', required=False)
    total_transfer = fields.Integer(string='Total transfer', required=False)
    insurance = fields.Integer(string='Insurance', required=False)
    difference = fields.Integer(string='Difference', required=False)
    item_and_qty = fields.Integer(string='Item And Qty', required=False)
    payment_condition = fields.Char(string='Payment condition', required=False)
    incoterms = fields.Many2one('account.incoterms', string='Incoterms', required=False)
    project_name = fields.Char(string='Project name', required=False)
    acid_no = fields.Integer(string='Acid No', required=False)
    importer_id = fields.Integer(string='Importer ID', required=False)
    exporter_id = fields.Integer(string='Exporter ID', required=False)
    for_warder = fields.Char(string='For warder', required=False)
    shipping_amount = fields.Integer(string='Shipping Amount', required=False)
    type_of_freight = fields.Char(string='Type Of Freight', required=False)
    shipping_line = fields.Char(string='Shipping Line', required=False)
    vessel = fields.Char(string='Vessel', required=False)
    release_letter = fields.Char(string='Release letter', required=False)
    container_size = fields.Integer(string='Container size', required=False)
    gross_weight = fields.Integer(string='Gross Weight', required=False)
    container_no = fields.Integer(string='Container NO', required=False)
    free_days = fields.Integer(string='Free Days', required=False)
    seal_no = fields.Integer(string='Seal.NO', required=False)
    mbl = fields.Char(string='MBL', required=False)
    hbl = fields.Char(string='HBL', required=False)
    pol = fields.Char(string='POL', required=False)
    pod = fields.Char(string='POD', required=False)
    transit_time = fields.Integer(string='Transit Time', required=False)
    free_of_demurrage = fields.Integer(string='Free OF Demurrage', required=False)
    loading_date = fields.Datetime(string='Loading Date', required=False)
    cut_off_date = fields.Datetime(string='Cut Off Date', required=False)
    etd = fields.Datetime(string='ETD', required=False)
    eta = fields.Datetime(string='ETA', required=False)
    docs_tracking_no = fields.Integer(string='Docs Tracking No', required=False)
    estimated_delivery = fields.Datetime(string='Estimated Delivery', required=False)
    # Arabic date Fields
    received_date_original_doc = fields.Datetime(string='تاريخ استلام النصر للمستندات الاصليه', required=False)
    send_date_bank_doc = fields.Datetime(string='تاريخ ارسال المستندات الاصليه الي البنك ', required=False)
    received_date_bank_doc = fields.Datetime(string='تاريخ استلام المستندات من البنك', required=False)
    send_date_customs_broker = fields.Datetime(string='تاريخ ارسال المستندات الي المخلص', required=False)
    tell_date_customs_broker = fields.Datetime(string='تاريخ ابلاغ المخلص القيم الجمركية', required=False)
    issuance_date_cheque = fields.Datetime(string='تاريخ اصدار الحسابات للشيكات الجمركية', required=False)
    release_date_shipment = fields.Datetime(string='تاريخ الافراج عن الشحنه', required=False)
    appointment_date = fields.Datetime(string='تاريخ التعيين', required=False)
    permission_date_shipment = fields.Datetime(string='تاريخ استلام اذن استلام المخزن للشحنه', required=False)
    details_process_tree = fields.One2many('details.fields', 'relation_id2', string="Details Fields")
    bill_count_field = fields.Integer(compute='compute_bill_count', default=0)
    payment_count_field = fields.Integer(compute='compute_pyment_count', default=0)
    po_count_field = fields.Integer(compute='compute_po_count', default=0)
    received_count_field = fields.Integer(compute='compute_received_count', default=0)
    get_notification_ids = fields.Many2one('date.notification', string='Get notification ids', required=False)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('close', 'Close'),
        ('done', 'Open'),
    ], string='Status', default='draft')

    def compute_bill_count(self):
        for rec in self:
            rec.bill_count_field = self.env['account.move'].search_count([])

    def compute_pyment_count(self):
        for rec in self:
            rec.payment_count_field = self.env['account.payment'].search_count([])

    def compute_po_count(self):
        for rec in self:
            rec.po_count_field = self.env['purchase.order'].search_count([])

    def compute_received_count(self):
        for rec in self:
            rec.received_count_field = self.env['stock.picking'].search_count([])

    # record.vehicle_count = self.env['fleet.vehicle'].search_count(
    #     [('driver_id', '=', self.id)])

    # Sequance Code
    # @api.model
    # def create(self, vals_list):
    #     vals_list['seq_no'] = self.env['ir.sequence'].next_by_code('shipment.data')
    #     return super(ShipmentData, self).create(vals_list)

    @api.onchange('suppliers')
    def default_collage(self):

        count_no = self.env['shipment.data'].search_count([])

        if count_no == 0:
            for rec in self:
                sup_get = rec.suppliers.name
                sup_get_ccc = str(sup_get)
            sup_get_2 = sup_get_ccc[0:2]
            year = datetime.now().year
            rec.seq_no = str(sup_get_2) + '-' + str(year) + '-' + '00' + str('1')

        else:
            last_id = self.env['shipment.data'].search([], order='id desc')[0].id

            last_id_2 = last_id + 1
            for rec in self:
                sup_get = rec.suppliers.name
                sup_get_ccc = str(sup_get)
            sup_get_2 = sup_get_ccc[0:2]
            year = datetime.now().year
            rec.seq_no = str(sup_get_2) + '-' + str(year) + '-' + '00' + str(last_id_2)

    def action_open_bills(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bills',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            # 'domain': [('shipments_bill', '=', self.id)],
            # 'context': "{'create': False}"
        }

    def action_open_payments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bills',
            'view_mode': 'tree,form',
            'res_model': 'account.payment',
            # 'domain': [('shipments_bill', '=', self.id)],
            # 'context': "{'create': False}"
        }

    def action_open_po(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bills',
            'view_mode': 'tree,form',
            'res_model': 'purchase.order',
            # 'domain': [('shipments_bill', '=', self.id)],
            # 'context': "{'create': False}"
        }

    def action_open_received(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bills',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            # 'domain': [('shipments_bill', '=', self.id)],
            # 'context': "{'create': False}"
        }

    def create_notification(self):
        for rec in self:
            rec_id = rec.id
            rec_name = rec.seq_no
            self.rec_id_save = rec.id

        self.env['date.notification'].create({
            'shipment_id': rec_id,
            'shipment_name': rec_name
        })

    @api.model
    def create(self, vals_list):
        record = super(ShipmentData, self).create(vals_list)
        # record.create_notification()
        record.shipment_date_notification()
        return record

    def open_shipment(self):
        for rec in self:
            rec.state = 'done'
            self.write_not()

    def close_shipment(self):
        for rec in self:
            rec.state = 'close'
            self.delete_not()

    def draft_shipment(self):
        for rec in self:
            rec.state = 'draft'

    def in_pro_shipment(self):
        for rec in self:
            rec.state = 'in_progress'

    @api.model
    def get_activity_mark(self):

        todo = []

        models_ids = self.env['mail.activity'].search_read(
            [('date_deadline', '=', datetime.now().date())])

        get_len = len(models_ids)

        get_date = models_ids[0]['create_date']

        get_date = models_ids[0]['create_date']
        get_date2 = str(get_date)
        get_date_3 = get_date2[0:10]

        d1 = datetime.strptime(str(get_date_3), "%Y-%m-%d")
        d2 = datetime.strptime(str(models_ids[0]['date_deadline']), "%Y-%m-%d")
        d3 = d2 - d1
        total_days = str(d3.days)

        if models_ids:
            for rec in range(get_len):
                # if models_ids[0]['res_id'] == models_ids[0]['res_id']:
                    todo.append(
                        {
                            'res_id': models_ids[rec]['res_id'],
                            'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                            'user_id': 2,
                            'summary': models_ids[rec]['summary'],
                            'note': models_ids[rec]['note'],
                            'activity_type_id': 4,
                            # 'date_deadline': datetime.now().today(),
                            'date_deadline': datetime.now() + timedelta(days=int(total_days)),
                        }
                    )

            return self.env['mail.activity'].create(todo)

    # @api.onchange('state')
    def write_not(self):
        for rec in self:
            get_state = rec.state
        if get_state == 'done':
            todos = 0
            # get_not_no = 0
            context = self._context
            current_uid = context.get('uid')
            # user = self.env['res.users'].browse(current_uid)

            for rec in self:
                rec_id = rec.rec_id_save
                state_shipment = self.state

            if state_shipment == 'close':
                return ''
            else:

                # get_data = self.env['date.notification'].search_read([('shipment_id', '=', rec_id)])
                get_data = self.env['date.notification'].search_read([])

                if get_data[0]['received_date_original_doc'] == 0:
                    pass
                else:
                    get_not_no = get_data[0]['received_date_original_doc']
                    date_deadline = datetime.now() + timedelta(days=get_not_no)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ استلام النصر للمستندات الاصليه',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline,
                    })

                if get_data[0]['send_date_bank_doc'] == 0:
                    pass
                else:
                    get_not_no_2 = get_data[0]['send_date_bank_doc']
                    date_deadline_2 = datetime.now() + timedelta(days=get_not_no_2)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ ارسال المستندات الاصليه الي البنك',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_2,
                    })

                if get_data[0]['received_date_bank_doc'] == 0:
                    pass
                else:
                    get_not_no_3 = get_data[0]['received_date_bank_doc']
                    date_deadline_3 = datetime.now() + timedelta(days=get_not_no_3)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ استلام المستندات من البنك',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_3,
                    })

                if get_data[0]['send_date_customs_broker'] == 0:
                    pass
                else:
                    get_not_no_4 = get_data[0]['send_date_customs_broker']
                    date_deadline_4 = datetime.now() + timedelta(days=get_not_no_4)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ ارسال المستندات الي المخلص',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_4,
                    })

                if get_data[0]['tell_date_customs_broker'] == 0:
                    pass
                else:
                    get_not_no_5 = get_data[0]['tell_date_customs_broker']
                    date_deadline_5 = datetime.now() + timedelta(days=get_not_no_5)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ ابلاغ المخلص القيم الجمركية',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_5,
                    })

                if get_data[0]['issuance_date_cheque'] == 0:
                    pass
                else:
                    get_not_no_6 = get_data[0]['issuance_date_cheque']
                    date_deadline_6 = datetime.now() + timedelta(days=get_not_no_6)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ اصدار الحسابات للشيكات الجمركية',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_6,
                    })

                if get_data[0]['release_date_shipment'] == 0:
                    pass
                else:
                    get_not_no_7 = get_data[0]['release_date_shipment']
                    date_deadline_7 = datetime.now() + timedelta(days=get_not_no_7)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ الافراج عن الشحنه',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_7,
                    })

                if get_data[0]['appointment_date'] == 0:
                    pass
                else:
                    get_not_no_8 = get_data[0]['appointment_date']
                    date_deadline_8 = datetime.now() + timedelta(days=get_not_no_8)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ التعيين',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_8,
                    })

                if get_data[0]['permission_date_shipment'] == 0:
                    pass
                else:
                    get_not_no_9 = get_data[0]['permission_date_shipment']
                    date_deadline_9 = datetime.now() + timedelta(days=get_not_no_9)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'تاريخ استلام اذن استلام المخزن للشحنه',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_9,
                    })

                if get_data[0]['loading_date'] == 0:
                    pass
                else:
                    get_not_no_10 = get_data[0]['loading_date']
                    date_deadline_10 = datetime.now() + timedelta(days=get_not_no_10)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'Loading Date',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_10,
                    })

                if get_data[0]['cut_off_date'] == 0:
                    pass
                else:
                    get_not_no_11 = get_data[0]['cut_off_date']
                    date_deadline_11 = datetime.now() + timedelta(days=get_not_no_11)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'Cut Off Date',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_11,
                    })

                if get_data[0]['etd'] == 0:
                    pass
                else:
                    get_not_no_12 = get_data[0]['etd']
                    date_deadline_12 = datetime.now() + timedelta(days=get_not_no_12)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'ETD',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_12,
                    })

                if get_data[0]['eta'] == 0:
                    pass
                else:
                    get_not_no_13 = get_data[0]['eta']
                    date_deadline_13 = datetime.now() + timedelta(days=get_not_no_13)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'ETA',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_13,
                    })

                if get_data[0]['estimated_delivery'] == 0:
                    pass
                else:
                    get_not_no_14 = get_data[0]['estimated_delivery']
                    date_deadline_14 = datetime.now() + timedelta(days=get_not_no_14)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'Estimated Delivery',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_14,
                    })

                if get_data[0]['po_date'] == 0:
                    pass
                else:
                    get_not_no_15 = get_data[0]['po_date']
                    date_deadline_15 = datetime.now() + timedelta(days=get_not_no_15)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'Po Date',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_15,
                    })

                if get_data[0]['pi_date'] == 0:
                    pass
                else:
                    get_not_no_16 = get_data[0]['pi_date']
                    date_deadline_16 = datetime.now() + timedelta(days=get_not_no_16)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'Pi Date',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_16,
                    })

                if get_data[0]['inv_date'] == 0:
                    pass
                else:
                    get_not_no_17 = get_data[0]['inv_date']
                    date_deadline_17 = datetime.now() + timedelta(days=get_not_no_17)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'Inv Date',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_17,
                    })

                if get_data[0]['value_date'] == 0:
                    pass
                else:
                    get_not_no_18 = get_data[0]['value_date']
                    date_deadline_18 = datetime.now() + timedelta(days=get_not_no_18)

                    self.env['mail.activity'].create({
                        'res_id': rec_id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                        'user_id': current_uid,
                        'summary': 'اشعار جديد',
                        'note': 'Value Date',
                        'activity_type_id': 4,
                        # 'date_deadline': datetime.now().today(),
                        'date_deadline': date_deadline_18,
                    })


    @api.onchange('state')
    def delete_not(self):
        for rec in self:
            get_state = rec.state
            rec_id = rec.rec_id_save
        if get_state == 'close':
            self.env['mail.activity'].search([('res_id', '=', rec_id)]).unlink()


    # @api.model
    def shipment_date_notification(self):
        todos = 0
        # get_not_no = 0
        context = self._context
        current_uid = context.get('uid')
        # user = self.env['res.users'].browse(current_uid)

        for rec in self:
            rec_id = rec.id
            rec_id_2 = rec.ids
            rec.rec_id_save = rec_id
            state_shipment = self.state

        if state_shipment == 'close':
            return ''
        else:

            # get_data = self.env['date.notification'].search_read([('shipment_id', '=', rec_id)])
            get_data = self.env['date.notification'].search_read([])

            if get_data[0]['received_date_original_doc'] == 0:
                pass
            else:
                get_not_no = get_data[0]['received_date_original_doc']
                date_deadline = datetime.now() + timedelta(days=get_not_no)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ استلام النصر للمستندات الاصليه',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline,
                })

            if get_data[0]['send_date_bank_doc'] == 0:
                pass
            else:
                get_not_no_2 = get_data[0]['send_date_bank_doc']
                date_deadline_2 = datetime.now() + timedelta(days=get_not_no_2)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ ارسال المستندات الاصليه الي البنك',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_2,
                })

            if get_data[0]['received_date_bank_doc'] == 0:
                pass
            else:
                get_not_no_3 = get_data[0]['received_date_bank_doc']
                date_deadline_3 = datetime.now() + timedelta(days=get_not_no_3)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ استلام المستندات من البنك',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_3,
                })

            if get_data[0]['send_date_customs_broker'] == 0:
                pass
            else:
                get_not_no_4 = get_data[0]['send_date_customs_broker']
                date_deadline_4 = datetime.now() + timedelta(days=get_not_no_4)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ ارسال المستندات الي المخلص',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_4,
                })

            if get_data[0]['tell_date_customs_broker'] == 0:
                pass
            else:
                get_not_no_5 = get_data[0]['tell_date_customs_broker']
                date_deadline_5 = datetime.now() + timedelta(days=get_not_no_5)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ ابلاغ المخلص القيم الجمركية',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_5,
                })

            if get_data[0]['issuance_date_cheque'] == 0:
                pass
            else:
                get_not_no_6 = get_data[0]['issuance_date_cheque']
                date_deadline_6 = datetime.now() + timedelta(days=get_not_no_6)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ اصدار الحسابات للشيكات الجمركية',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_6,
                })

            if get_data[0]['release_date_shipment'] == 0:
                pass
            else:
                get_not_no_7 = get_data[0]['release_date_shipment']
                date_deadline_7 = datetime.now() + timedelta(days=get_not_no_7)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ الافراج عن الشحنه',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_7,
                })

            if get_data[0]['appointment_date'] == 0:
                pass
            else:
                get_not_no_8 = get_data[0]['appointment_date']
                date_deadline_8 = datetime.now() + timedelta(days=get_not_no_8)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ التعيين',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_8,
                })

            if get_data[0]['permission_date_shipment'] == 0:
                pass
            else:
                get_not_no_9 = get_data[0]['permission_date_shipment']
                date_deadline_9 = datetime.now() + timedelta(days=get_not_no_9)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'تاريخ استلام اذن استلام المخزن للشحنه',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_9,
                })

            if get_data[0]['loading_date'] == 0:
                pass
            else:
                get_not_no_10 = get_data[0]['loading_date']
                date_deadline_10 = datetime.now() + timedelta(days=get_not_no_10)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'Loading Date',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_10,
                })

            if get_data[0]['cut_off_date'] == 0:
                pass
            else:
                get_not_no_11 = get_data[0]['cut_off_date']
                date_deadline_11 = datetime.now() + timedelta(days=get_not_no_11)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'Cut Off Date',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_11,
                })

            if get_data[0]['etd'] == 0:
                pass
            else:
                get_not_no_12 = get_data[0]['etd']
                date_deadline_12 = datetime.now() + timedelta(days=get_not_no_12)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'ETD',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_12,
                })

            if get_data[0]['eta'] == 0:
                pass
            else:
                get_not_no_13 = get_data[0]['eta']
                date_deadline_13 = datetime.now() + timedelta(days=get_not_no_13)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'ETA',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_13,
                })

            if get_data[0]['estimated_delivery'] == 0:
                pass
            else:
                get_not_no_14 = get_data[0]['estimated_delivery']
                date_deadline_14 = datetime.now() + timedelta(days=get_not_no_14)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'Estimated Delivery',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_14,
                })

            if get_data[0]['po_date'] == 0:
                pass
            else:
                get_not_no_15 = get_data[0]['po_date']
                date_deadline_15 = datetime.now() + timedelta(days=get_not_no_15)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'Po Date',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_15,
                })

            if get_data[0]['pi_date'] == 0:
                pass
            else:
                get_not_no_16 = get_data[0]['pi_date']
                date_deadline_16 = datetime.now() + timedelta(days=get_not_no_16)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'Pi Date',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_16,
                })

            if get_data[0]['inv_date'] == 0:
                pass
            else:
                get_not_no_17 = get_data[0]['inv_date']
                date_deadline_17 = datetime.now() + timedelta(days=get_not_no_17)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'Inv Date',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_17,
                })

            if get_data[0]['value_date'] == 0:
                pass
            else:
                get_not_no_18 = get_data[0]['value_date']
                date_deadline_18 = datetime.now() + timedelta(days=get_not_no_18)

                self.env['mail.activity'].create({
                    'res_id': rec_id,
                    'res_model_id': self.env['ir.model'].search([('model', '=', 'shipment.data')]).id,
                    'user_id': current_uid,
                    'summary': 'اشعار جديد',
                    'note': 'Value Date',
                    'activity_type_id': 4,
                    # 'date_deadline': datetime.now().today(),
                    'date_deadline': date_deadline_18,
                })

class DetailsData(models.Model):
    _name = 'details.data'
    _inherit = 'shipment.data'
    _description = 'Details Data'

    # name = fields.Char()
    details_process_tree = fields.One2many('details.fields', 'relation_id', string="Details Fields")


class DetailsFields(models.Model):
    _name = 'details.fields'
    _description = 'Details Fields'

    # follow_up_date = fields.Datetime(string='Date', required=False, default=datetime.now(), readonly=True)
    follow_up_text = fields.Text(string='Follow up', required=False)
    relation_id = fields.Many2one('details.data', string='Details Data')
    relation_id2 = fields.Many2one('shipment.data', string='Details Data')

    def default_date(self):
        return datetime.now()

    follow_up_date = fields.Datetime(string='Date', required=False, default=default_date, readonly=True)
