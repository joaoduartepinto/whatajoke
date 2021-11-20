import click
from whatajoke.joke_service.joke_service import get_joke
from whatajoke.whatsapp_service.whatsapp_service import send_message


@click.command()
@click.option("--group", "-g",
              required=True,
              prompt="Name of the group or person to send the joke to",
              help="Name of the group or person to send the joke to!")
@click.option("--category", "-c",
              type=click.Choice(['any', 'programming', 'misc', 'dark', 'pun', 'spooky', 'christmas'],
                                case_sensitive=False),
              default="any",
              help="Category of the joke. Default value is \"any\".")
@click.option("--flag", "-f",
              type=click.Choice(['none', 'nsfw', 'religious', 'political', 'racist', 'sexist', 'explicit'],
                                case_sensitive=False),
              default="none",
              help="Flag to add to category. Default value is \"none\".")
def send_joke(group, category, flag):
    """

    :param group:
    :param category:
    :param flag:
    :return:
    """
    # Parse choice to String
    category = str(category)
    flag = str(flag)

    # Get joke from joke service
    joke = get_joke(category, flag)
    click.echo(joke)

    # Send joke to Whatsapp Service
    click.echo(group)
    send_message(group, joke)


def main():
    send_joke()
