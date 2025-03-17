from odoo import models,fields,api
# importem la llibreria 
from datetime import datetime

class LabModel(models.Model):
    _name = "lab.model"  # nom de la taula
    _description = "Model Laboratori" # descripció de la taula

    # camps creats per a la taula lab.model
    codi = fields.Char('Codi mostra')
    nom = fields.Char('Nom mostra')
    descripcio = fields.Text('Descripció')
   
    data = fields.Date('Data Obtenció')
    # definim el camp en el qual posarem informació
    hora = fields.Char('Hora')
    # relacionem la taula res.partner amb la taula lab.model 
    # i la product.product amb la taula lab.model
    client_id = fields.Many2one('res.partner','Client')
    product_id = fields.Many2one('product.product','Producte')

    # 1. Camps d'entrada
    pes_envas = fields.Float('Pes de envas')
    pes_producte = fields.Float('Pes del producte')
    # 2.- definim el camp a calcular
    pes_total = fields.Float('Pes Total')
    pes_total = fields.Float(compute='_func_calcular',string='Pes Total',store=True)
    
    # Definim la funció a realitzar els càlculs
    @api.depends('pes_envas','pes_producte')
    def _func_calcular(self): 
        self.pes_total= self.pes_envas + self.pes_producte

    # Definim una mètode public de la classe LabModel que el cridarem amb un botó
    def getHora(self):
       # Obtenir la data i hora actual amb format
        self.hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Depurar hora actural
        print("########## Data i Hora actural:", self.hora)
        return True

    def funcioExemple(self):
        print("Això o podeu veure a la línica de depuració, Exemple de mètode")
        return True