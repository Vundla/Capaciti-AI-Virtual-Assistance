import datetime

def greet_user():
    print("👋 Hello! I'm HealthMate, your virtual healthcare assistant.")
    print("How can I help you today?\n")

def get_user_input():
    return input("You: ").lower()

def handle_query(query):
    if "headache" in query:
        return "🧠 It sounds like you have a headache. Make sure you're hydrated and consider resting. If it persists, consult a doctor."
    elif "fever" in query:
        return "🌡️ A fever could indicate an infection. Monitor your temperature and stay hydrated."
    elif "reminder" in query or "medication" in query:
        return set_reminder()
    elif "appointment" in query:
        return set_appointment()
    elif "thank" in query:
        return "😊 You're welcome! Stay healthy!"
    else:
        return "🤖 I'm still learning. Please try asking something else."

def set_reminder():
    med = input("What medication do you want to be reminded about? ")
    time = input("At what time should I remind you? (HH:MM format) ")
    return f"⏰ Reminder set for {med} at {time}."

def set_appointment():
    date = input("Enter the appointment date (YYYY-MM-DD): ")
    time = input("Enter the appointment time (HH:MM): ")
    return f"📅 Appointment scheduled for {date} at {time}."

if __name__ == "__main__":
    greet_user()
    while True:
        query = get_user_input()
        if query in ["exit", "quit", "bye"]:
            print("👋 Goodbye! Take care.")
            break
        response = handle_query(query)
        print(f"HealthMate: {response}\n")

