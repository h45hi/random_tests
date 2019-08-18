import requests, time, yagmail, os, ipdb

while True:
	try:
		with open("erp_status.log", "a") as e:
			e.write("Date: {} Time: {} Response: {}\n".format(time.strftime("%d-%m-%Y"), time.strftime("%H-%M-%S"), requests.get("http://103.99.16.70:8069/")))
			time.sleep(10)
			ipdb.set_trace()
	except Exception:
		password = os.environ.get('ERP_PASS')
		sender_email = os.environ.get('ERP_MAIL')
		receiver_email = os.environ.get('OFFICE_MAIL')
		current_time = time.strftime("%H-%M-%S")
		subject = "ERP Site Alert on " + current_time
		body = "Please check ERP website, it has some issue."

		yag = yagmail.SMTP(sender_email, password)

		yag.send(
		    to=receiver_email,
		    subject=subject,
		    contents=body,
		)

		print("Email has been sent !")
		break