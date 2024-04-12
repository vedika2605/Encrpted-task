# Copyright (c) 2024, vedika and contributors
# For license information, please see license.txt
import frappe
import base64
from frappe.model.document import Document

class AdharCard(Document):
    ENCRYPT_PREFIX = "#ENCRYPTED#"

    def validate(self):
        if self.aadhar_card and not self.aadhar_card.startswith(self.ENCRYPT_PREFIX):
            self.encrypt_aadhar()

    def encrypt_aadhar(self):
        self.aadhar_card = self.ENCRYPT_PREFIX + base64.b64encode(self.aadhar_card.encode()).decode()

    def decrypt_aadhar(self):
        if self.aadhar_card and self.aadhar_card.startswith(self.ENCRYPT_PREFIX):
            self.aadhar_card = base64.b64decode(self.aadhar_card[len(self.ENCRYPT_PREFIX):]).decode()
			
