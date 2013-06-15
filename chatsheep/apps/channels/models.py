from django.db import models

import datetime


class Channel(models.Model):

    name = models.CharField(
        max_length=100,
    )

    period = models.IntegerField(
        default=30,
        help_text='The time period to look back over when checking if a message has been sent too many times recently.'
    )

    frequency = models.IntegerField(
        default=5,
        help_text='The maximum amount of times a message is allowed to be sent within the time period.'
    )

    def __unicode__(self):
        return self.name


class WhitelistedWord(models.Model):

    channel = models.ForeignKey(Channel)

    word = models.TextField()

    def __unicode__(self):
        return self.word[:15]


class Message(models.Model):

    message = models.TextField(

    )

    hash = models.CharField(
        max_length=1000,
        db_index=True
    )

    sender = models.CharField(
        max_length=1000,
    )

    channel = models.ForeignKey(
        Channel,
    )

    datetime = models.DateTimeField(
        auto_now_add=True,
        default=datetime.datetime.now
    )

    def __unicode__(self):
        return self.message
