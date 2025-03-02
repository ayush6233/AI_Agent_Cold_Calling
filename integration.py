import datetime

class CalendarIntegration:
    def check_availability(self, slot):
        return True

    def schedule_demo(self, slot, customer_name):
        return f"Demo scheduled for {customer_name} on {slot['date']} at {slot['start_time']}."

class CRMIntegration:
    def update_candidate_info(self, conv_id, field, value):
        pass

    def schedule_followup_interview(self, conv_id):
        pass

class PaymentSystemIntegration:
    def process_payment(self, order_id, amount, payment_method="upi"):
        return True

# Default instances for ease of use
calendar_integration = CalendarIntegration()
crm_integration = CRMIntegration()
payment_integration = PaymentSystemIntegration()
