from calendar import c
from dataclasses import fields
from django.forms import ModelForm
from dashboard.models import Barang, Membership
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            "kodebrg" : forms.TextInput({'class':'form-control'}),
            "nama" : forms.TextInput({'class':'form-control'}),
            "stok" : forms.NumberInput({'class':'form-control'}),
            "harga" : forms.TextInput({'class':'form-control'}),
            "link_gbr" : forms.TextInput({'class':'form-control'}),
            "jenis_id" : forms.Select({'class':'form-control'}),
        }

class FormMembership(ModelForm):
    class Meta :
        model=Membership
        fields='__all__'

        widgets = {
            "kodemem" : forms.TextInput({'class':'form-control'}),
            "nama" : forms.TextInput({'class':'form-control'}),
            "status" : forms.Select({'class':'form-control'}),
            "level_id" : forms.Select({'class':'form-control'}),

        }
