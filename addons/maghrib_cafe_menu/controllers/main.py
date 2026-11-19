import json
from odoo import http
from odoo.http import request


class MaghribCafeController(http.Controller):

    @http.route('/api/v1/menu', type='http', auth='public', methods=['GET', 'OPTIONS'], csrf=False, cors='*')
    def get_menu(self, **kwargs):
        categories = request.env['maghrib.cafe.category'].sudo().search([('active', '=', True)])
        payload = []
        for cat in categories:
            items = []
            for item in cat.item_ids.filtered(lambda i: i.active):
                items.append({
                    'id': item.id,
                    'name': item.name,
                    'description': item.description or '',
                    'price_mad': item.price_mad,
                    'qty_available': item.qty_available,
                    'is_available': item.is_available,
                })
            payload.append({
                'id': cat.id,
                'code': cat.code or '',
                'name': cat.name,
                'service_hours': cat.service_hours or '',
                'items': items,
            })
        return request.make_response(
            json.dumps({'status': 'success', 'currency': 'MAD', 'data': payload}),
            headers=[('Content-Type', 'application/json')],
        )