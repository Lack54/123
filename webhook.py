from requests.exceptions import Timeout
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
def main(title, discription, color):
    webhook = DiscordWebhook(url="webhook", timeout=10)
    embed = DiscordEmbed(title=title, description=discription, color=color)




    webhook.add_embed(embed)
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSK3PKHAicBFg8G-7KeKA5n7XZuy8EnBsEWdg&usqp=CAU")
    # execute the webhook
    try:
        response = webhook.execute()
    except Timeout:
        return

