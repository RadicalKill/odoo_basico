from odoo import models, fields, api
from odoo.exceptions import ValidationError


class basico(models.Model):
    _name= 'odoo_basico.informacion'
    _description = 'Exemplo basico'
    _sql_constraints = [('nome_unico', 'unique(name)', 'Non se pode repetir o nome')]

    name=fields.Char(string="Titulo:")
    descripcion=fields.Text(string="A Descripcion")
    literal = fields.Char(store=False)
    Alto=fields.Integer(string="Alto en centimentros")
    Largo = fields.Integer(string="Largo en centimentros")
    Ancho = fields.Integer(string="Ancho en centimentros")
    Volumen = fields.Float(compute="_Volumen", store=True)
    Peso=fields.Float(string="Peso en Kg.s",default= 2.7, digits=(6,2))
    Densidad= fields.Float(compute="_Densidad", store=True)
    Autorizado=fields.Boolean(string="¿Autorizado?", default= True)
    Fecha=fields.Datetime(string="Data e hora",default= lambda self: fields.Datetime.now())
    Sexo_traducido = fields.Selection([("Hombre", "Home"), ("Mujer", "Muller"), ("Otros", "Outros")], string="Sexo")

    @api.depends('Alto', 'Largo', 'Ancho')
    def _Volumen(self):
        for rexistro in self:
            rexistro.Volumen = float(rexistro.Alto) * float(rexistro.Largo) * float(rexistro.Ancho)

    @api.depends('Peso','Volumen')
    def _Densidad(self):
        for rexistro in self:
            if rexistro.Volumen!=0:
              rexistro.Densidad = 100 * (float(rexistro.Peso))/ (float(rexistro.Volumen))
            else: rexistro.Densidad=0

    @api.onchange('Alto')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.Alto > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.Alto
            else:
                rexistro.literal = ""

    @api.constrains('Peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
    def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.Peso < 1 or rexistro.Peso > 4:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)