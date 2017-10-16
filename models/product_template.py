from odoo import api, fields, models


class ProductTemplate(models.Model):
	_inherit = "product.template"

	ket_uom_id = fields.Many2one('product.uom', 'Unit of Measure')