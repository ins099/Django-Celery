from django import forms

from task2.tasks import send_review_email_task

class ReviewForm(forms.Form):
    name = forms.CharField(
        label='FirstName', widget=forms.TextInput(
            attrs={'class':'form-control mb-3', 'id':'form-firstname'}))
    email = forms.EmailField(max_length= 100, widget= forms.TextInput(
            attrs = {'class':'form-control mb-3', 'id':'form-email'}))
    review = forms.CharField(
            label = "Review", widget = forms.Textarea(attrs = {'class': 'form-control', 'rows':5}))

    def send_email(self):
            send_review_email_task.delay(
                    self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review'])
