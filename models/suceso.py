from odoo import models, fields, api



class basico(models.Model):
    _name= 'odoo_basico.suceso'
    _description = 'Exemplo suceso'

    name=fields.Char(string="Titulo:")
    descripcion=fields.Text(string="A Descripcion")
    nivel=fields.Selection([("Bajo", "Baixo"), ("Medio", "Medio"), ("Alto", "Alto")], string="Nivel")
    data_hora=fields.Datetime(string="Data e hora",default= lambda self: fields.Datetime.now())
