from django.core.management.base import BaseCommand
from users.models import DummyUser
from zoneinfo import ZoneInfo


class Command(BaseCommand):
    help = "Convert Pakistan time to UTC"

    def handle(self, *args, **kwargs):

        users = DummyUser.objects.all()

        for user in users:

            pkt = user.pakistan_time.replace(
                tzinfo=ZoneInfo("Asia/Karachi")
            )

            utc = pkt.astimezone(ZoneInfo("UTC"))

            user.utc_time = utc
            user.save()

        self.stdout.write(
            self.style.SUCCESS("All users converted to UTC successfully!")
        )