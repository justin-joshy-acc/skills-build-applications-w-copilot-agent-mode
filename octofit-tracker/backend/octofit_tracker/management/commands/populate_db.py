from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Workouts
        pushup = Workout.objects.create(name='Pushup', description='Pushup exercise', difficulty='easy')
        run = Workout.objects.create(name='Run', description='Running', difficulty='medium')

        # Activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=steve, activity_type='pushup', duration=15, date=timezone.now())
        Activity.objects.create(user=bruce, activity_type='run', duration=25, date=timezone.now())
        Activity.objects.create(user=clark, activity_type='pushup', duration=20, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=bruce, points=110)
        Leaderboard.objects.create(user=clark, points=95)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
