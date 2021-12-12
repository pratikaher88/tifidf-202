from django import forms

class DocumentForm(forms.Form):
    document_1 = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 4, 'placeholder':'Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation.'}), required=False)
    document_2 = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 4, 'placeholder':'What is your p-value for the heteroskedasticity test, and is it significant?'}), required=False )
    document_3 = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 4, 'placeholder':'Is the regression significant? How do you know?'}), required=False )
    document_4 = forms.CharField( widget=forms.Textarea(attrs={'cols': 100, 'rows': 4},), required=False )