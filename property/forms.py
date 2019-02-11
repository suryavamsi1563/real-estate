from django import forms
from .models import Contacted,PropertyTable,PropertyDetails


class ContactForm(forms.Form):
    issue_choices = (
        ('SELL', 'Selling a property'),
        ('BUY', 'Buying Related'),
        ('CONTACT', 'Contacting Seller or Buyer'),
    )
    name = forms.CharField(
                    widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    issue_type = forms.ChoiceField(choices=issue_choices,widget=forms.Select(attrs={'class':'form-control'}))
    issue = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    bot_field = forms.CharField(required=False,widget=forms.HiddenInput)


    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 20:
            raise forms.ValidationError("Name too long")
        return name

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(str(mobile)) != 10:
            raise forms.ValidationError("Mobile number must be 10 digits only.")
        return mobile
    
    def clean_bot_field(self):
        bot = self.cleaned_data['bot_field']
        if bot:
            raise forms.ValidationError("We dont allow Scrapping.")
        return bot


class ContactModalForm(forms.ModelForm):
    class Meta():
        model = Contacted
        # fields = "__all__"
        exclude = ['bot_field']

class botform(forms.Form):
    bot_field = forms.CharField(required=False,widget=forms.HiddenInput)
    def clean_bot_field(self):
        bot = self.cleaned_data['bot_field']
        if bot:
            raise forms.ValidationError("We dont allow Scrapping.")
        return bot

class SellPropertyForm(forms.ModelForm):

    class Meta():
        model = PropertyTable
        fields = "__all__"


class PropertyDetailsForm(forms.ModelForm):
    class Meta():
        model = PropertyDetails
        exclude = ['property_id']