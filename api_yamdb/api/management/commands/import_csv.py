import csv

from django.core.management.base import BaseCommand

from reviews.models import Category, Genre, Title, Review, Comment
from users.models import User


class Command(BaseCommand):
    data_dir = 'static/data/'
    filenames_models = {
        'category.csv': Category,
        'genre.csv': Genre,
        'titles.csv': Title,
        'genre_title.csv': Title.genre.through,
        'users.csv': User,
        'review.csv': Review,
        'comments.csv': Comment
    }

    def handle(self, *args, **options):
        for name, Model in self.filenames_models.items():
            objs = []
            with open((self.data_dir + name), encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    obj = Model(**row)
                    objs.append(obj)
            Model.objects.bulk_create(objs)
