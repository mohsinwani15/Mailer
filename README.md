
# Mailer

This Python script sends an HTML email using Gmail's SMTP server. It allows you to customize the email content using a template and send it to any recipient.

## Features

- Sends HTML-formatted emails.
- Allows dynamic message insertion into an HTML template.
- Uses Gmail's SMTP server for email delivery.

## Prerequisites

- Python 3.x
- Gmail account with either:
  - Basic credentials (email and password) **or**
  - 2-Step Verification enabled and an app password.

## Setup Instructions

1. **Download the Script and HTML Template**

   Make sure you have the following files in the same directory:
   
   - `script.py` (the Python script)
   - `index.html` (the HTML template file)

2. **Prepare the HTML Template**

   Create an `index.html` file with the following content:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Email</title>
     </head>
     <body>
       $Message
     </body>
   </html>
   ```

3. **Update the Script**

   Open the `script.py` file and update the following line with your Gmail credentials:

   ```python
   smtp.login('your_email@gmail.com', 'your_password')
   ```

   - Replace `'your_email@gmail.com'` with your Gmail address.
   - Replace `'your_password'` with your Gmail password or app password.

   **Security Note:** Avoid hardcoding sensitive information in the script. Consider using environment variables.

## How to Use

1. **Run the Script**

   Execute the script from the command line with the following arguments:

   ```bash
   python script.py recipient_email@example.com "Subject Here" "Your message here"
   ```

   - `recipient_email@example.com`: The recipient's email address.
   - `"Subject Here"`: The subject of the email.
   - `"Your message here"`: The message body to be included in the email.

2. **Example Command**

   ```bash
   python script.py john.doe@example.com "Greetings!" "Hello, this is a test email."
   ```

   This will send an email with the subject "Greetings!" and the message "Hello, this is a test email." to `john.doe@example.com`.

## Troubleshooting

- **SMTP Authentication Error:** Ensure that you have enabled "Less secure app access" in your Gmail account settings, or use an app password if you have 2-Step Verification enabled.

- **FileNotFoundError:** Ensure that the `index.html` file is in the same directory as the script.

## Security Recommendations

- **Environment Variables:** Store your email credentials in environment variables rather than hardcoding them in the script.

- **App Passwords:** If you have 2-Step Verification enabled on your Gmail account, use an app password instead of your regular Gmail password.

## License

This script is provided "as-is" without any warranty. Use it at your own risk.

