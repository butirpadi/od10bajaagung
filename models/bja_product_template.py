from odoo import models, fields, api
# from odoo.addons.base.res.res_partner import FormatAddress

class ProductTemplate(models.Model):
    _inherit = "product.template"

    cost_per_weight = fields.Float('Cost per Weight')

    @api.onchange('standard_price')
    def _std_price_change(self):
    	for prod in self:
    		if prod.standard_price == 0 or prod.weight == 0:
    			prod.cost_per_weight = 0
    		else:
    			prod.cost_per_weight = prod.standard_price / prod.weight

    @api.onchange('cost_per_weight')
    def _cow_price_change(self):
    	for prod in self:
    		prod.standard_price = prod.cost_per_weight * prod.weight

    @api.onchange('weight')
    def _weight_change(self):
    	for prod in self:
    		prod._std_price_change()
    		prod._cow_price_change()
