from odoo import models, fields, api
# from odoo.addons.base.res.res_partner import FormatAddress

# class Partner(models.Model, FormatAddress):
class Partner(models.Model):
    _inherit = "res.partner"

    salesman = fields.Boolean(string='Salesperson', default=False)