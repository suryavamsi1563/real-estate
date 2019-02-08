from django import forms

class testform(forms.Form):
    number = forms.IntegerField()

    def clean_number(self):
        if self.cleaned_data['number'] > 2:
            raise forms.ValidationError("Number greater than 2")
        return self.cleaned_data['number']