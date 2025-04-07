```python
class NotificationService:
    def __init__(self, communication_channel, logger):
        self.communication_channel = communication_channel
        self.logger = logger

    def send_notification(self, customer, loan_details):
        message = self._create_message(loan_details)
        delivery_status = self.communication_channel.send(customer.contact_info, message)
        self.logger.log(delivery_status)

    def _create_message(self, loan_details):
        return (
            f"Loan Approved!\n"
            f"Amount: {loan_details['amount']}\n"
            f"Interest Rate: {loan_details['interest_rate']}%\n"
            f"Repayment Period: {loan_details['repayment_period']} months\n"
            f"Next Step: Please accept the loan offer to proceed with your car purchase."
        )

class EmailChannel:
    def send(self, email, message):
        # Simulate sending email
        print(f"Sending email to {email}:\n{message}")
        return "Email sent successfully"

class SMSChannel:
    def send(self, phone_number, message):
        # Simulate sending SMS
        print(f"Sending SMS to {phone_number}:\n{message}")
        return "SMS sent successfully"

class InAppChannel:
    def send(self, user_id, message):
        # Simulate sending in-app notification
        print(f"Sending in-app notification to user {user_id}:\n{message}")
        return "In-app notification sent successfully"

class Logger:
    def log(self, message):
        # Simulate logging
        print(f"Log: {message}")

# Example usage
customer = {
    'contact_info': 'customer@example.com',  # Could be email, phone number, or user ID
    'preferred_channel': 'email'
}

loan_details = {
    'amount': 25000,
    'interest_rate': 3.5,
    'repayment_period': 60
}

logger = Logger()
channel = EmailChannel() if customer['preferred_channel'] == 'email' else SMSChannel() if customer['preferred_channel'] == 'sms' else InAppChannel()
notification_service = NotificationService(channel, logger)
notification_service.send_notification(customer, loan_details)
```