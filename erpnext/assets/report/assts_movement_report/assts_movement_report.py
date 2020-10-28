# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	data    = get_data(filters)
	return columns, data





def get_columns(filters):
	columns = [
		{
			"label": _("Asset Name"),
			"fieldname": "asset_name",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Employee"),
			"fieldname": "employee",
			"fieldtype": "Link",
			"options":"Employee",
			"width": 150
		},
	
		{
			"label": _("value"),
			"fieldname": "value",
			"fieldtype": "Data",
			"width": 150
		},
		
		
	]
	

	return columns

def get_data(filters):
	condition=""
	if filters.get("asset_name"):
		condition +="AND tabAsset.name = '%s'"%filters.get("asset_name")
	if filters.get("employee_name"):
		condition += " AND tabAsset.custodian = '%s' "%filters.get("employee_name")


	print(condition)
	results=frappe.db.sql("""  
			SELECT
			tabAsset.`name` as 'asset_name', 
			tabEmployee.`employee_name` as 'employee',
			tabAsset.value_after_depreciation as value
		FROM
			tabAsset
			INNER JOIN
			tabEmployee
			
		WHERE
			tabAsset.custodian NOT LIKE ""
			{condition}
	""".format(condition=condition) ,as_dict=1)

	return results
