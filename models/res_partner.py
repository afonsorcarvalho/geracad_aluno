# -*- coding: utf-8 -*-

from odoo import models, fields, api


class geracad_aluno(models.Model):
   
    
    _inherit = ['res.partner']

    name = fields.Char()
    value = fields.Integer()
    nome_pai = fields.Char("Nome do Pai")
    nome_mae = fields.Char("Nome da mãe")
    data_nascimento = fields.Date("Data de Nascimento")
    escolaridade = fields.Char()


    e_aluno = fields.Boolean(string='É aluno')
    
    
    observacoes = fields.Text("Observações")
   
