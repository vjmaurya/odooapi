url = 'http://localhost:8069' #<insert server URL>
db = 'testdb' #<insert database name>
username = 'admin'
password = 'admin' #<insert password for your admin user (default: admin)>

import xmlrpclib
from datetime import datetime


common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
print("Logged In User ID",uid)
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

class Customer(): 
    def read(self):
        # Read customers
        model_name = 'res.partner'
        partner_ids = models.execute_kw(db, uid, password, model_name, 'search', [[['customer', '=', True]]])
        partner_records = models.execute_kw(db, uid, password, model_name, 'read', [partner_ids])
        return partner_records

    def create(self):
        # Create customer
        model_name = 'res.partner'
        vals = {
            'name': "New Customer",
        }
        new_id = models.execute_kw(db, uid, password, model_name, 'create', [vals])
        return new_id

    def update(self, id):
        # Update customer
        model_name = 'res.partner'
        models.execute_kw(db, uid, password, model_name, 'write', [[id], {
            'name': "Newer partner"
        }])

cust = Customer()
print("New customer ID: ",cust.create())
