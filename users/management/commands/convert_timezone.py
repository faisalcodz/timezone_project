from django.db import transaction
from django.core.management.base import BaseCommand
from users.models import DummyUser
from zoneinfo import ZoneInfo


class Command(BaseCommand):
    help = "Convert Pakistan time to UTC"

    def handle(self, *args, **kwargs):

        with transaction.atomic():

            users = DummyUser.objects.all()

            for user in users:

                # PKT
                pkt = user.pakistan_time.replace(
                    tzinfo=ZoneInfo("Asia/Karachi")
                )

                # PKT → UTC
                utc = pkt.astimezone(ZoneInfo("UTC"))

                # UTC → PKT
                pkt_again = utc.astimezone(
                    ZoneInfo("Asia/Karachi")
                )

                user.utc_time = utc
                user.converted_back_time = pkt_again

                user.save()

        self.stdout.write(
            self.style.SUCCESS(
                "All users converted PKT → UTC → PKT successfully!"
            )
        )