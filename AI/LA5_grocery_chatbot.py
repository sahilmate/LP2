import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # A dictionary of regex patterns mapped to responses
    responses = {
        r"(hi|hello|hey)": 
            "Hello! Welcome to our Grocery store. How can I help you today?",
        r"(order status|track order)": 
            "Please provide your order ID to check the status.",
        r"(shipping time|delivery time)": 
            "We offer same-day delivery and standard shipping (3-5 business days).",
        r"(return policy)": 
            "You can return items within 7 days if unopened. Need help with a return?",
        r"(milk)": 
            "Milk is 30rs per liter.",
        r"(eggs)": 
            "A dozen eggs cost 80rs.",
        r"(rice)": 
            "Rice is 50rs per kg.",
        r"(vegetables|veggies)": 
            "We have fresh vegetables available. Which ones are you looking for?",
        r"(fruits)": 
            "We have apples, bananas, and oranges in stock. Which one do you need?",
        r"(snacks)": 
            "We have chips, biscuits, and chocolates available.",
        r"(beverages|drinks)": 
            "We have soft drinks, juices, and bottled water. What would you like?",
        r"(payment methods)": 
            "We accept cash, credit/debit cards, and UPI payments.",
        r"(store hours|timing)": 
            "Our store is open from 8 AM to 10 PM every day.",
        r"(location|address)": 
            "We are located at XYZ Market, Main Street, City.",
        r"(bye|exit)": 
            "Goodbye! Happy shopping! 🛍️"
    }

    # Match user input against each pattern
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    # Fallback if no pattern matches
    return "I am sorry, I didn't understand that. Can you rephrase or ask about a specific grocery item?"

def main():
    print("🛒 Welcome to our Grocery Chatbot! Type 'exit' to end the conversation.")

    while True:
        user_message = input("You: ")
        
        if user_message.lower() in ["exit", "bye"]:
            print("Chatbot: Goodbye! Happy shopping! 🛍️")
            break

        response = chatbot_response(user_message)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()






"""
This code implements an elementary chatbot for a grocery ordering application.
"""

from nltk.chat.util import Chat, reflections

# Define some patterns and responses
groceries = {
    'Fruits': ['Apples', 'Bananas', 'Oranges'],
    'Vegetables': ['Tomatoes', 'Potatoes', 'Carrots'],
    'Dairy': ['Milk', 'Cheese', 'Butter']
}

patterns = [
    (r'hi|hello|hey', 
     ['Hello! How can I assist you today?', 'Hey there! Looking to order some groceries?', 'Hi! Ready to shop for groceries?']),
    (r'how are you', 
     ['I am just a bot, but I am here to help you with your grocery shopping!', 'I am doing great, thanks for asking. How can I assist you today?']),
    (r'(.*) groceries', 
     ['Here are the categories available: ' + ', '.join(groceries.keys()) + '. What would you like to order?']),
    (r'(.*) items', 
     ['Here are the items available in each category:' + f"{category}: {', '.join(items)}" for category, items in groceries.items()]),
    (r'(.*) order', 
     ['Sure! Let\'s proceed with placing your order.']),
    (r'(.*) (bye|goodbye)', 
     ['Thank you for visiting Grocery ChatBot. Have a great day!', 'Goodbye! Enjoy your groceries!', 'Bye! See you soon.']),
]

# create a chatbot
grocery_bot = Chat(patterns, reflections)


def place_order(category, items, quantity):
    # calculate total bill
    item_price = 50  # assuming a fixed price per item for now
    total_bill = quantity * item_price
    return f"Order confirmed! You have ordered {quantity} {items} from {category}.\nTotal amount: Rs. {total_bill}."


def main():
    print("\nHello! Welcome to Grocery ChatBot. How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        response = grocery_bot.respond(user_input)
        print("ChatBot:", response)
        
        # extract information for placing an order
        if "order" in user_input.lower():
            category = input("Which category would you like to order from? :")
            items = input("What item would you like to order? :")
            quantity = int(input("How many units do you need? :"))
            order_response = place_order(category, items, quantity)
            print("ChatBot:", order_response)
        
        # check if the user wants to end the conversation
        if any(word in user_input.lower() for word in ['bye', 'goodbye']):
            break


main()
