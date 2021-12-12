from django import forms

class DocumentForm(forms.Form):
    document_1 = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 4}), required=False)
    document_2 = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 4}), required=False )
    document_3 = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 4}), required=False )
    document_4 = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 4}), required=False )