import requests
import whatajoke.joke.url_helper as url_helper
import whatajoke.joke.joke_formatter as joke_formatter


# https://sv443.net/jokeapi/v2/#try-it


def get_joke(category, flag):
    # Get formatted url
    url = url_helper.get_url(category, flag)

    # Send request
    response = requests.get(url)
    print(response.content)

    # Format joke
    joke = joke_formatter.format_joke(response)

    print(joke)
    return joke
