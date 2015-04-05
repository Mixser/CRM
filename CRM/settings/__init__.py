import os

ENV = os.environ.get('ENV', 'DEV')

if ENV == 'DEV':
    from crm.settings.dev import *
elif ENV == 'STAGING':
    from staging import *
elif ENV == 'PROD':
    from prod import *