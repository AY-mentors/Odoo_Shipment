{
    'name': 'ElNaser Shipment',
    'version': '16.0.0',
    'summary': 'Summery',
    'description': 'Shipment Data',
    'category': 'Category',
    'author': 'Author',
    'website': 'Website',
    'sequence': -100,
    'license': 'LGPL-3',
    'depends': ['base', 'purchase', 'account_accountant', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'data/cron.xml',
        'data/activity.xml',
        'views/shipment_data_view.xml',
        'views/accounting_inherit_view.xml',
        'views/date_notification_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
