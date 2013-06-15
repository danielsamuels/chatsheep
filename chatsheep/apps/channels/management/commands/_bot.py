import datetime
import hashlib

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
from django.utils.timezone import now

from ...models import Channel, Message, WhitelistedWord


class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, password=None, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, password)], nickname, nickname)
        self.channel = '#{}'.format(channel)
        self.channel_item = Channel.objects.get(
            name=channel
        )

    def on_welcome(self, c, e):
        print 'Joining {}'.format(self.channel)
        c.join(self.channel)

    def on_privmsg(self, c, e):
        if e.source == 'jtv!jtv@jtv.tmi.twitch.tv' and e.target == self._nickname:
            # The server is telling us something.
            print 'Message from server: {}'.format(e.arguments[0])

        if e.target == self.channel:
            self.handle_chat(e.source, e.arguments[0])

    def on_pubmsg(self, c, e):
        if e.target == self.channel:
            self.handle_chat(e.source, e.arguments[0])

    def handle_chat(self, sender, message):
        sender = sender.split('!')[0]
        hashed = hashlib.sha1(message).hexdigest()

        # Save the message into the database.
        Message.objects.create(
            message=message,
            hash=hashed,
            channel=self.channel_item,
            sender=sender
        )

        # If this message is on the whitelist, then don't worry about it.
        try:
            WhitelistedWord.objects.get(
                channel=self.channel_item,
                word=message
            )

        except:
            # Check to see if this phrase has been sent too frequently.
            freq = Message.objects.filter(
                hash=hashed,
                datetime__gte=now() - datetime.timedelta(seconds=self.channel_item.period)
            ).count()

            print '{} has been sent {} times in the last {} seconds'.format(message, freq, self.channel_item.period)
            print freq, self.channel_item.frequency

            if freq > self.channel_item.frequency:
                self.connection.privmsg(self.channel, '.timeout {} 1'.format(sender))
