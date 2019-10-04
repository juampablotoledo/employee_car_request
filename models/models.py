# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CarRequest(models.Model):
    _name = 'car.request' #Crea una tabla con ese nombre en la base de datos
    _inherit = ['mail.thread']
    _description = 'Request a vehicle'
#   El atributo string determina lo que se verá de forma predeterminada cuando estemos llenando el formulario
    name = fields.Char(string="Request", required=True, )
#   En el atributo default de la entrada date_from se define una variable que se encuentra en odoo/odoo/fields.py para usar el tiempo presente desde una variable ya declarada por el framework
    date_from = fields.Datetime(string="Starting date", default=fields.Datetime.now, )
    date_to = fields.Datetime(string="End date", required=False, )
#   En el atributo comodel_name del campo many2one se coloca el identificador de la relación, éste lo podemos encontrar en la URL del módulo que estamos llamando desde el navegador
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Solicitant Employee", required=True, )
    car_id = fields.Many2one(comodel_name="fleet.vehicle", string="Vehicle", required=True, )
#   El campo odoo_fields_selection sirve para determinar el estado en el que se encuentra una solicitud para determinar el flujo de trabajo
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'), ('confirm', 'Confirm'),
                                                         ('validate', 'Validate'), ('refuse', 'Refuse'),
                                                         ('approved', 'Approved'), ], default="draft", track_visibility='onchange')

    @api.multi
    def confirm_request(self):
        self.state = 'confirm'\

    @api.multi
    def validate_request(self):
        self.state = 'validate'\

    @api.multi
    def refuse_request(self):
        self.state = 'refuse'

    @api.multi
    def approve_request(self):
        self.state = 'approved'
