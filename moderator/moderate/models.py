from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db.models import signals as dbsignals
from django.dispatch import receiver

from uuslug import uuslug


class MozillianProfile(models.Model):
    """Mozillians User Profile"""
    user = models.OneToOneField(User, related_name='userprofile')
    slug = models.SlugField(blank=True, max_length=100)
    username = models.CharField(max_length=40)
    avatar_url = models.URLField(max_length=400, default='')

    def __unicode__(self):
        return self.username

    class Meta:
        ordering = ['username']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = uuslug(self.username, instance=self)
        super(MozillianProfile, self).save(*args, **kwargs)


@receiver(dbsignals.post_save, sender=User,
          dispatch_uid='create_user_profile_sig')
def create_user_profile(sender, instance, created, raw, **kwargs):
    if not raw:
        up, created = MozillianProfile.objects.get_or_create(user=instance)
        if not created:
            dbsignals.post_save.send(sender=MozillianProfile, instance=up,
                                     created=created, raw=raw)


class Event(models.Model):
    """Event model."""
    name = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = uuslug(self.name, instance=self)
        super(Event, self).save(*args, **kwargs)

    @property
    def questions_count(self):
        return self.questions.all().count()


class Question(models.Model):
    """Question relational model."""
    asked_by = models.ForeignKey(User)
    event = models.ForeignKey(Event, related_name='questions')
    question = models.TextField(validators=[MaxLengthValidator(140),
                                            MinLengthValidator(10)])

    def __unicode__(self):
        return u'Question {pk} from {user}'.format(pk=self.id, user=self.asked_by)


class Vote(models.Model):
    """Vote model."""
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question, related_name='votes')
    date_voted = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question')

    def __unicode__(self):
        return u'Vote of {user} for {question}'.format(user=self.user, question=self.question)
