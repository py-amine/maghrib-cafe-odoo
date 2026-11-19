from odoo import api, fields, models


class CafeCategory(models.Model):
    _name = 'maghrib.cafe.category'
    _description = 'Cafe Menu Category'
    _order = 'sequence, name'

    name = fields.Char(string='Catégorie', required=True)
    code = fields.Char(string='Code (01..06)')
    service_hours = fields.Char(string='Horaires de service')
    sequence = fields.Integer(string='Ordre', default=10)
    active = fields.Boolean(default=True)
    item_ids = fields.One2many('maghrib.cafe.item', 'category_id', string='Produits')
    item_count = fields.Integer(string='Nombre de produits', compute='_compute_item_count')

    @api.depends('item_ids')
    def _compute_item_count(self):
        for rec in self:
            rec.item_count = len(rec.item_ids)


class CafeMenuItem(models.Model):
    _name = 'maghrib.cafe.item'
    _description = 'Cafe Menu Item'
    _order = 'category_id, sequence, name'

    name = fields.Char(string='Nom du produit', required=True)
    description = fields.Text(string='Description / Ingrédients')
    price_mad = fields.Float(string='Prix (MAD)', required=True, default=0.0)
    qty_available = fields.Integer(string='Stock disponible', default=20)
    is_available = fields.Boolean(
        string='Disponible',
        compute='_compute_is_available',
        store=True,
    )
    sequence = fields.Integer(string='Ordre', default=10)
    active = fields.Boolean(default=True)
    category_id = fields.Many2one(
        'maghrib.cafe.category',
        string='Catégorie',
        required=True,
        ondelete='restrict',
    )

    @api.depends('qty_available')
    def _compute_is_available(self):
        for rec in self:
            rec.is_available = rec.qty_available > 0

    def action_set_out_of_stock(self):
        self.write({'qty_available': 0})

    def action_restock_ten(self):
        for rec in self:
            rec.qty_available += 10