# -*- coding: utf-8 -*-
from odoo import models, fields, api


class OdooLibrary(models.Model):
    _name = 'odoo.library'
    _description = 'Odoo Library'

    name = fields.Char(string='Judul Buku', required=True)
    category = fields.Selection([
        ('umum','Umum'),
        ('IT','IT'),
        ('kesehatan','Kesehatan'),
        ('politik','Politik')
        ], string='Kategori', default='umum', required=True)
    publish_date = fields.Date(string='Tanggal Terbit', required=True)
    code = fields.Text(string='Kode ISBN', required=True)
    amount = fields.Integer(string='Jumlah Buku', required=True)
    user_id = fields.Many2one('res.users', string="Penulis")
    transaction_line = fields.One2many('library.transaction', 'library_id', string='Transaksi')

class LibraryTransaction(models.Model):
    _name = 'library.transaction'
    _description = 'Library Transaction'

    library_id = fields.Many2one('odoo.library', string='Buku', required=True, ondelete='cascade')
    name = fields.Char(string='Nama Peminjam', required=True)
    location = fields.Text(string='Lokasi')
    quantity = fields.Integer(string='Jumlah Buku Dipinjam', required=True)
    start_date = fields.Date(string='Tanggal Pinjam', required=True)
    end_date = fields.Date(string='Tanggal Pengembalian', required=True)
    cost = fields.Float(string='Total Biaya', required=True)

    def action_print_transaction(self):
        return self.env.ref('odoo_library.report_library_transaction_action').report_action(self)
    
class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(string='Nama', required=True)
    id_type = fields.Selection([
        ('ktp','KTP'),
        ('sim','SIM'),
        ('pasport','Pasport')
        ], string='Jenis Kartu Identitas', default='ktp', required=True, help='Jenis Identitas')
    id_number = fields.Text(string='Nomor Identitas')