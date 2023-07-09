import csv
import smtplib
from email.mime.text import MIMEText

# Set up SMTP connection
smtp_server = 'smtp.mycompany.co.za'
smtp_port = 587
smtp_username = 'your_username'
smtp_password = 'your_password'

smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# Read CSV file
csv_file = open('users.csv', 'r')
csv_reader = csv.reader(csv_file)

# Loop through each row in CSV and generate email for each user
for row in csv_reader:
    display_name = row[0]
    email_address = row[1]
    password = row[2]

    # Generate email message
    message = 'Dear {0},\n\nHere is your unique password: {1}\n\nBest regards,\nYour Company'.format(display_name, password)
    email = MIMEText(message)
    email['Subject'] = 'Your Password for Our Company'
    email['From'] = 'your_company@mycompany.co.za'
    email['To'] = email_address

    # Send email
    smtp_connection.sendmail('your_company@mycompany.co', [email_address], email.as_string())

# Close SMTP connection and CSV file
smtp_connection.quit()
csv_file.close()
