from django import forms
from django_localflavor_br.froms import BRCPFField, BRCNPJField


class FormCliente(forms.Form):
	cpf = BRCPFField(required = True)



