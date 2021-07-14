from django.core.management.base import BaseCommand

from telegram.services.bot_manage import bot


class Command(BaseCommand):
    help = 'Activate telegram bot'

    def handle(self, *args, **options):
        bot.polling(none_stop=True)
