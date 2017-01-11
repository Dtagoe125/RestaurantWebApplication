from django import forms
from django.core.mail import EmailMessage




class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.CharField(widget=forms.EmailInput(), required=True)
	subject = forms.CharField(required=True)
	body = forms.CharField(widget=forms.Textarea(), required=True)


	def send_message(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		subject = self.cleaned_data['subject']
		body = self.cleaned_data['body']

		message = '''
				New Message from {name} @ {email}
				Subject: {subject}
				Message:
				{body}
				'''.format(name=name,
					email=email,
					subject=subject,
					body=body)

		email_msg = EmailMessage('New Contact Form Submission',
					message,
					email,
					['dtagoe125@gmail.com'])

		email_msg.send()