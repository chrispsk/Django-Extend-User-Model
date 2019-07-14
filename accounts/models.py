from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


# def validate_author_email(value):
#     if "@" in value:
#         return value
#     else:
#         raise ValidationError("Not a valid email!!!!!")

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=120, null=True, blank=True)
    #author_email = models.CharField(max_length=220, validators=[validate_author_email, validate_chris], null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
    instance.profile.save()

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
