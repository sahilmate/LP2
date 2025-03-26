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


"""
This code implements an elementary chatbot for a bus ticket booking application.
"""

from nltk.chat.util import Chat, reflections

# Define some patterns and responses
buses = {
    'Mumbai to Pune': ['Morning: 8:00 AM', 'Afternoon: 1:00 PM', 'Evening: 6:00 PM'],
    'Delhi to Jaipur': ['Morning: 7:00 AM', 'Afternoon: 12:00 PM', 'Evening: 5:00 PM'],
    'Bangalore to Chennai': ['Morning: 9:00 AM', 'Afternoon: 2:00 PM', 'Evening: 7:00 PM']
}

patterns = [
    (r'hi|hello|hey', 
     ['Hello! How can I assist you today?', 'Hey there! Looking to book a bus ticket?', 'Hi! Ready to plan your journey?']),
    (r'how are you', 
     ['I am just a bot, but I am here to help you book bus tickets!', 'I am doing great, thanks for asking. How can I assist you today?']),
    (r'(.*) route', 
     ['Here are the available routes: ' + ', '.join(buses.keys()) + '. Which route would you like to book?']),
    (r'(.*) ticket', 
     ['How many tickets do you need?', 'Sure! How many tickets would you like to book?', 'Got it! How many tickets do you want to book?']),
    (r'(.*) timing', 
     ['Here are the timings for each route:' + f"{route}: {', '.join(timings)}" for route, timings in buses.items()]),
    (r'(.*) book tickets', 
     ['Sure! Let\'s proceed with booking tickets.']),
    (r'(.*) (bye|goodbye)', 
     ['Thank you for visiting RedBus ChatBot. Have a safe journey!', 'Goodbye! Enjoy your trip!', 'Bye! See you soon.']),
]

# create a chatbot
redbus_bot = Chat(patterns, reflections)


def book_tickets(route, tickets, timing):
    # calculate total bill
    ticket_price = 500  # assuming a fixed price for now
    total_bill = tickets * ticket_price
    return f"Booking confirmed! You have booked {tickets} tickets for {route} at {timing}.\nTotal amount: Rs. {total_bill}."


def main():
    print("\nHello! Welcome to RedBus ChatBot. How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        response = redbus_bot.respond(user_input)
        print("ChatBot:", response)
        
        # extract information for booking tickets
        if "book tickets" in user_input.lower():
            route = input("Which route would you like to book? :")
            tickets = int(input("How many tickets do you need? :"))
            timing = input("At what time would you like to travel? :")
            booking_response = book_tickets(route, tickets, timing)
            print("ChatBot:", booking_response)
        
        # check if the user wants to end the conversation
        if any(word in user_input.lower() for word in ['bye', 'goodbye']):
            break


main()
