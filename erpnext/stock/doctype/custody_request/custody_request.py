# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Custodyrequest(Document):






	# @frappe.whitelist() 
	def create_asset_movement(self):
		doc = frappe.new_doc('Asset Movement')
		doc.company = self.company
		# doc.purpose = ''
		if self.reference_document_type == "Employee" :
			doc.purpose = 'Issue'
		else :
			doc.purpose = 'Transfer'

		doc.save()
		frappe.db.commit()
		

		return doc

@frappe.whitelist() 
def create_asset_movement(name , *args,**kwargs):
		frm = frappe.get_doc("Custody request" , name)
		doc = frappe.new_doc('Asset Movement')
		doc.company = frm.company
		# doc.purpose = ''
		if frm.reference_document_type == "Employee" :
			doc.purpose = 'Issue'
		else :
			doc.purpose = 'Transfer'

		doc.reference_doctype = "Custody request"
		doc.reference_name = name

		# doc.save()
		# frappe.db.commit()
		

		return (doc)