# -*- coding: utf-8 -*-

from odoo import models, fields, api


class geracad_aluno(models.Model):
   
    
    _inherit = ['res.partner']

    name = fields.Char()
    
    nome_pai = fields.Char("Nome do Pai")
    nome_mae = fields.Char("Nome da mãe")
    data_nascimento = fields.Date("Data de Nascimento")
    escolaridade = fields.Char()
    rg = fields.Char("RG")
    rg_data_expedicao = fields.Date("Data Exp. RG")
    sexo = fields.Selection([('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')])
    


    e_aluno = fields.Boolean(string='É aluno')
    e_professor = fields.Boolean(string='É professor')
    ponto_referencia_endereco = fields.Char("Ponto de Referência")
    
    
    observacoes = fields.Text("Observações")

    
   
