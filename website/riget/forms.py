from django import forms

class nyFetPerson(forms.Form):
	firstname = forms.CharField(label="fornavn")
	lastname = forms.CharField(label="lastname")
	CPR = forms.CharField(label="CPR")
	FDG = forms.BooleanField(label="FDG", required=False)
	avastin = forms.BooleanField(label="avastin", required=False)
		
