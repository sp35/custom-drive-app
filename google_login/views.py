from django.shortcuts import render
from django.contrib.auth.models import User as user
import re

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def glogin(request):
	return render(request, 'google_login/login.html')

def login_success(request):
	if user.is_authenticated:
		org = (re.findall('\S+@\S+', str(request.user.email)))[0].split('@')[1]

		if org == 'pilani.bits-pilani.ac.in':
			sender_email = os.getenv('SENDER_EMAIL')
			message = Mail(
				from_email=sender_email,
				to_emails=str(request.user.email),
				subject=f'Dear User',
				html_content=f'<strong><em>Thanks for using our services!</em></strong></p>')

			try:
				sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
				response = sg.send(message)
				print(response.status_code)
				print(response.body)
				print(response.headers)
			except Exception as e:
				print(e.message)

			return render(request, 'google_login/logged_in.html')

		else:
			return render(request, 'google_login/not_bits_id.html')
 
	