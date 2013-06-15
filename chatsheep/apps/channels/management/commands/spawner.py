import irc
import threading
import logging

from django.core.management import BaseCommand

from ...models import Channel
from ._bot import TestBot

# FORMAT = '%(asctime)-15s %(message)s'
# logging.basicConfig(
#     level=logging.DEBUG,
#     format=FORMAT
# )
# logger = logging.getLogger('irc.client')


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for channel in Channel.objects.all():
            thread = threading.Thread(
                target=self.join_irc,
                name=channel.name,
                kwargs={
                    'channel': channel.name
                }
            )

            if not thread.is_alive():
                thread.start()

    def join_irc(self, *args, **kwargs):
        name = kwargs['channel']

        # Move twitch password into setting, or env var.
        bot = TestBot(name, 'chatsheep', '{}.jtvirc.com'.format(name), "twitchpasswordgoeshere")
        bot.start()
