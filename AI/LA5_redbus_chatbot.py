import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # A dictionary of regex patterns mapped to responses
    responses = {
        r"(hi|hello|hey)": 
            "Hello! Welcome to Redbus. How can I help you today?",
        r"(book.*ticket)": 
            "Sure, let's get started with your booking. Where are you traveling from?",
        r"(bus schedule|bus timings|bus time)": 
            "Our buses operate throughout the day. Please specify your route for exact timings.",
        r"(cancel.*ticket)": 
            "Please provide your ticket ID to cancel your booking.",
        r"(refund)": 
            "Refunds usually take 3-5 business days to process after cancellation.",
        r"(change.*seat)": 
            "You can change seats before finalizing the booking. Need help with that?",
        r"(contact.*support|help)": 
            "You can reach our support at 1800-XXX-XXXX or email support@redbus.com.",
        r"(bye|exit)": 
            "Goodbye! Have a safe journey!"
    }

    # Match user input against each pattern
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    # Fallback if no pattern matches
    return "I'm sorry, I didn't quite catch that. Could you rephrase?"

def main():
    print("🚌 Welcome to the Redbus Chatbot! Type 'exit' anytime to end the conversation.")

    while True:
        user_message = input("You: ")
        
        if user_message.lower() in ["exit", "bye"]:
            print("Chatbot: Goodbye! Have a safe journey!")
            break

        response = chatbot_response(user_message)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()




'''
Uses a dictionary of regex patterns mapped to responses.

In the while True loop, it reads user input, checks for an “exit” condition, and calls chatbot_response.

The chatbot returns a matching response or a default fallback if no pattern is matched.
'''