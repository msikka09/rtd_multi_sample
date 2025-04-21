
import os

project = 'MyProject'

# Detect RTD project to set master_doc
rtd_project = os.environ.get('READTHEDOCS_PROJECT')

if rtd_project == 'l1':
    master_doc = 'L1/index'
elif rtd_project == 'l2':
    master_doc = 'L2/index'
else:
    master_doc = 'index'
