from django.contrib import admin

from models import Channel, Message, WhitelistedWord


class WhitelistedWordAdmin(admin.TabularInline):

    model = WhitelistedWord


class ChannelAdmin(admin.ModelAdmin):

    inlines = (WhitelistedWordAdmin,)


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Message)
