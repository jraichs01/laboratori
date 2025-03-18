from odoo import models,fields,api
from datetime import datetime # import datetime module

'''
    Definim la classe LabModel, que hereda de la classe models.Model de Odoo.
    Aquesta classe modelarà la nostra taula de la base de dades.
    Atributs : camps de la taula ( _<nom_atribut> : atributs privats)
    Metodes : funcions que es poden executar sobre la taula
'''

class LabModel(models.Model):
    _name = "lab.model"  # nom de la taula
    _description = "Model Laboratori" # descripció de la taula

    # camps creats per a la taula lab.model
    codi = fields.Char('Codi mostra')
    nom = fields.Char('Nom mostra')
    descripcio = fields.Text('Descripció')
   
    data = fields.Date('Data Obtenció') # camp de tipus data, es desplega Witchet
    hora = fields.Char('Hora')
    client_id = fields.Many2one('res.partner','Client') # relaciona amb la taula res.partner
    product_id = fields.Many2one('product.product','Producte') # relaciona amb la taula product.product
    pes_envas = fields.Float('Pes de envas')
    pes_producte = fields.Float('Pes del producte')
    pes_total = fields.Float('Pes Total') # camp calculat
    
    #camp calculat, cridem la funció que el calcula
    pes_total = fields.Float(compute='_func_calcular',string='Pes Total',store=True) # 
    
    # Definim el metode a realitzar els càlculs (metodes _<nom_metode> : en python són privats)
    @api.depends('pes_envas','pes_producte')
    def _func_calcular(self): 
        self.pes_total= self.pes_envas + self.pes_producte

    # Definim una mètode public de la classe LabModel que el cridarem amb un botó
    def getHora(self):
        self.hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # obtenim la hora actual
        print("########## Data i Hora actural:", self.hora) # per a veure el resultat a la consola
        return True

    # Metodes, cridem ACCIONS DEFINIDES a: meu_informe_action_report.xml 
    # Es criden a través de la vista de la taula lab.model definida a laboratori_view.xml
    def imprimirMostraPDF(self):
        return self.env.ref('laboratori.pdf_informe_action').report_action(self)
    
    def imprimirMostraHTML(self):
        return self.env.ref('laboratori.html_informe_action').report_action(self)
    
    def imprimirLlistaMostresHTML(self):
        return self.env.ref('laboratori.html_llistat_mostres_accio').report_action(self)
