from django import forms


# Contact Form Class
class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name',
                           widget=forms.TextInput(attrs={'class': "form-control mb-3", 'placeholder': "Enter Your Name"}))
    email = forms.CharField(label='Your Email', widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Enter Your Email", 'type': "email"}))
    message = forms.CharField(label='Message',
                              widget=forms.Textarea(attrs={'class': "form-control", 'rows': "7" ,'placeholder':"Leave "
                                                                                                               "your "
                                                                                                               "message here"}))
