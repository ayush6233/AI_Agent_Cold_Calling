import sys, time
from agent import AIAgent
from conversation_manager import ConversationManager
from tts_stt import text_to_speech, speech_to_text
from integration import CalendarIntegration, PaymentSystemIntegration

def run_demo():
    agent = AIAgent()
    conv = ConversationManager("demo_scheduling")
    calendar = CalendarIntegration()
    # Generate the initial prompt with placeholders
    prompt = agent.get_initial_prompt(
        "demo_scheduling",
        customer_name="Customer",
        company_name="TechSolutions",
        product_name="ERP Suite"
    )
    print("Agent:", prompt)
    # text_to_speech(prompt)
    
    # Ask user to provide slot details
    user_input = input("Please enter your available slot (format: YYYY-MM-DD, HH:MM, HH:MM): ")
    if user_input.lower() in ["exit", "quit"]:
        print("Agent:", agent.generate_farewell("demo_scheduling"))
        return
    conv.add_message("customer", user_input)
    
    # Parse the provided slot details
    try:
        date, start_time, end_time = [s.strip() for s in user_input.split(",")]
        slot = {"date": date, "start_time": start_time, "end_time": end_time}
    except Exception:
        print("Invalid input format. Please provide in the format: YYYY-MM-DD, HH:MM, HH:MM")
        return
    conv.update_state("slot", slot)
    
    # Schedule demo using the calendar integration
    demo_confirmation = calendar.schedule_demo(slot, "Customer")
    conv.update_state("demo_scheduled", True)
    conv.add_message("agent", demo_confirmation)
    print("Agent:", demo_confirmation)

def run_interview():
    agent = AIAgent()
    conv = ConversationManager("candidate_interviewing")
    prompt = agent.get_initial_prompt("candidate_interviewing", company_name="TechSolutions", position="Developer")
    print("Agent:", prompt)
    text_to_speech(prompt)
    user_input = input("You: ")
    conv.add_message("candidate", user_input)
    question = agent.generate_interview_question("introduction", conv.get_conversation_context())
    conv.add_message("agent", question)
    print("Agent:", question)

def run_payment():
    agent = AIAgent()
    conv = ConversationManager("payment_followup")
    payment_sys = PaymentSystemIntegration()
    prompt = agent.get_initial_prompt("payment_followup", customer_name="Raj Sharma", order_id="ORD001", amount=12500, due_date="2025-03-15")
    print("Agent:", prompt)
    text_to_speech(prompt)
    user_input = input("You: ")
    conv.add_message("customer", user_input)
    response = agent.generate_response("payment_followup", conv.get_conversation_context())
    conv.add_message("agent", response)
    print("Agent:", response)

def main():
    print("Select scenario:\n1. Demo Scheduling\n2. Candidate Interview\n3. Payment Follow-up")
    choice = input("Choice (1/2/3): ")
    if choice == "1":
        run_demo()
    elif choice == "2":
        run_interview()
    elif choice == "3":
        run_payment()
    else:
        print("Exiting.")

if __name__ == "__main__":
    main()
