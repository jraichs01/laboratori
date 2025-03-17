
# característiques generals del mòdul

{
    'name': 'Laboratori Control Qualitat',
    'version': '1.0',
    'author': 'Professor',
    'category': 'Qualitat',
    'description': 'Control de qualitat',
    'depends': ['base','product','web'],
    'data': [
        'security/ir.model.access.csv', 
        'views/laboratori_view.xml', 
        'views/meu_informe_action_report.xml', 
        'views/meu_informe_template.xml', 
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
