from django import forms

class QueryConfig(forms.Form):
    dateini = forms.DateField(help_text="Insira a data inicial",
                           input_formats=['%d/%m/%Y',
                                          '%d/%m/%y',
                                          '%Y-%m-%d'])
    datefim = forms.DateField(help_text="Insira a data final",
                           input_formats=['%d/%m/%Y',
                                          '%d/%m/%y',
                                          '%Y-%m-%d'])
    #est_mun = forms.CharField(help_text="Resultados agrupados por Estado (E)", max_length=1)
    keyword = forms.CharField(help_text = "Insira aqui o nome da doença a ser pesquisada", max_length = 50)

class KeyConfig(forms.Form):
    keyword = forms.CharField(help_text = "Digite o nome da doença a ser pesquisada", max_length = 50)
