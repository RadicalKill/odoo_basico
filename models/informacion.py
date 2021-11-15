from odoo import models, fields, api



class basico(models.Model):
    _name= 'odoo_basico.informacion'
    _description = 'Exemplo basico'

    name=fields.Char(string="Titulo:")
    descripcion=fields.Text(string="A Descripcion")
    Alto=fields.Integer(string="Alto en centimentros")
    Largo = fields.Integer(string="Largo en centimentros")
    Ancho = fields.Integer(string="Ancho en centimentros")
    Volumen= fields.Float(string="Volume")
    Peso=fields.Float(string="Peso en Kg.s",default= 2.7, digits=(6,2))
    Densidad= fields.Float(string="Densidade")
    Autorizado=fields.Boolean(string="¿Autorizado?", default= True)
    Fecha=fields.Date(string="Data e hora")
    Sexo_traducido = fields.Selection([("Hombre", "Home"), ("Mujer", "Muller"), ("Otros", "Outros")], string="Sexo")