from odoo import models, fields, api, Command, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_fodec = fields.Boolean(string="Soumis au FODEC (1%)", default=False)
    is_timbre = fields.Boolean(string="Timbre Fiscal (1 DT)", default=False)

    def _get_base_ht(self):
        """
        Computes the HT total excluding FODEC and Timbre lines,
        and excluding services because only industrial products are subject to FODEC.
        """
        self.ensure_one()
        fodec_product = self.env.ref('l10n_tn_invoice.product_fodec', raise_if_not_found=False)
        timbre_product = self.env.ref('l10n_tn_invoice.product_timbre_fiscal', raise_if_not_found=False)
        
        base_ht = 0.0
        for line in self.invoice_line_ids:
            if line.display_type != 'product':
                continue
            if line.product_id and line.product_id in [fodec_product, timbre_product]:
                continue
            # Tunisian rules: Only industrial products are subject to FODEC. Services are exempt.
            if line.product_id and line.product_id.type == 'service':
                continue
            base_ht += line.price_subtotal
            
        return base_ht

    @api.onchange('is_fodec')
    def _onchange_is_fodec(self):
        fodec_product = self.env.ref('l10n_tn_invoice.product_fodec', raise_if_not_found=False)
        if not fodec_product:
            return

        fodec_lines = self.invoice_line_ids.filtered(lambda l: l.product_id == fodec_product)
        if self.is_fodec:
            if not fodec_lines:
                base_ht = self._get_base_ht()
                fodec_amount = base_ht * 0.01

                self.update({'invoice_line_ids': [Command.create({
                    'product_id': fodec_product.id,
                    'quantity': 1,
                    'price_unit': fodec_amount,
                })]})
        else:
            if fodec_lines:
                self.invoice_line_ids -= fodec_lines

    @api.onchange('is_timbre')
    def _onchange_is_timbre(self):
        timbre_product = self.env.ref('l10n_tn_invoice.product_timbre_fiscal', raise_if_not_found=False)
        if not timbre_product:
            return

        timbre_lines = self.invoice_line_ids.filtered(lambda l: l.product_id == timbre_product)
        if self.is_timbre:
            if not timbre_lines:
                self.update({'invoice_line_ids': [Command.create({
                    'product_id': timbre_product.id,
                    'quantity': 1,
                    'price_unit': 1.0,
                })]})
        else:
            if timbre_lines:
                self.invoice_line_ids -= timbre_lines

    @api.onchange('invoice_line_ids')
    def _onchange_lines_recalcul_fodec(self):
        """ Auto-recalculates FODEC amount when other invoice lines change. """
        if not self.is_fodec:
            return
            
        fodec_product = self.env.ref('l10n_tn_invoice.product_fodec', raise_if_not_found=False)
        if not fodec_product:
            return

        fodec_line = self.invoice_line_ids.filtered(lambda l: l.product_id == fodec_product)
        if fodec_line:
            base_ht = self._get_base_ht()
            new_fodec_amount = base_ht * 0.01
            # Update the first found fodec line
            fodec_line[0].price_unit = new_fodec_amount
