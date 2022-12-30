import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # automatically set pub_date to today's date (auto_now)
    pub_date = models.DateTimeField("date published")

    def can_vote(self):
        """Test if voting is allowed for this poll question.

        :return: True if voting is allowed, False if not.
        """
        return timezone.now() >= self.pub_date

    def __str__(self):
        return self.question_text

    def is_published(self):
        now = timezone.now()
        return self.pub_date <= now

    @property
    def total_votes(self) -> int:
        """Total number of votes for this poll."""
        return sum(choice.votes for choice in self.choice_set.all())

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    @property
    def votes(self) -> int:
        """The number of votes for this Choice."""
        return Vote.objects.filter(choice=self).count()

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    """A vote by a user for a poll Question."""

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Vote for "{self.choice.choice_text}" by {self.user.username}'
