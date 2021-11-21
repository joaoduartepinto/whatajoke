from whatajoke.joke.joke_service import get_joke
from whatajoke.whatsapp.whatsapp_service import send_message


def send_joke(group, category, flag):
    # Get joke from joke service
    joke = get_joke(category, flag)

    # Send joke to Whatsapp Service
    send_message(group, joke)