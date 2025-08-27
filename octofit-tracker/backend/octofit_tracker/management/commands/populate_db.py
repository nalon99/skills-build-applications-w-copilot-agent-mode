from django.core.management.base import BaseCommand
from django.conf import settings
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel')
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC')

        # Activities
        Activity.objects.create(user='Iron Man', type='Running', duration=30)
        Activity.objects.create(user='Captain America', type='Cycling', duration=45)
        Activity.objects.create(user='Batman', type='Swimming', duration=60)
        Activity.objects.create(user='Superman', type='Yoga', duration=20)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=80)

        # Workouts
        Workout.objects.create(name='Hero HIIT', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', difficulty='Medium')
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
