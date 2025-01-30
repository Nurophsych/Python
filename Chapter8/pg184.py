# Function to display each message
def show_messages(messages):
    for message in messages:
        print(message)

# List of text messages
messages = ["Hello, how are you?", "I hope you're having a great day!", "Don't forget to bring the documents.", "See you soon!"]

# Calling the function to show the messages
show_messages(messages)







print('8-10')
# Function to send messages by printing them and moving them to another list
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()  # Remove a message from the original list
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)  # Add it to the sent messages list

# List of messages to send
messages = ["Hello, how are you?", "I hope you're having a great day!", "Don't forget to bring the documents.", "See you soon!"]
sent_messages = []

# Call the function to send the messages
send_messages(messages, sent_messages)

# Print both lists to ensure the messages have been moved
print("\nMessages that have been sent:")
print(sent_messages)

print("\nRemaining messages:")
print(messages)







print('8-11')
# Function to send messages by printing them and moving them to another list
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()  # Remove a message from the original list
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)  # Add it to the sent messages list

# List of messages to send
messages = ["Hello, how are you?", "I hope you're having a great day!", "Don't forget to bring the documents.", "See you soon!"]
sent_messages = []

# Make a copy of the messages list to send
messages_copy = messages[:]

# Call the function with the copy of the messages list
send_messages(messages_copy, sent_messages)

# Print both lists to ensure the original list is unchanged
print("\nMessages that have been sent:")
print(sent_messages)

print("\nRemaining messages (original list):")
print(messages)
