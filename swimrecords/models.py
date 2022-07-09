from django.db import models
from django.forms import ValidationError
from datetime import timedelta
from django.utils import timezone

def validate_first_name(first_name):
    if first_name == None:
        raise ValidationError()

def validate_last_name(last_name):
    if last_name == None:
        raise ValidationError()

def validate_team_name(team_name):
    if team_name == None:
        raise ValidationError()

def validate_relay(relay):
    if relay == None:
        raise ValidationError(f"{relay} value must be either True or False.")

def validate_stroke(stroke):
    valid_strokes = ['front crawl', 'butterfly', 'breast', 'back','freestyle']
    if stroke not in valid_strokes:
        raise ValidationError(f"{stroke} is not a valid stroke")

def validate_distance(distance):
    if distance < 50:
        raise ValidationError("Ensure this value is greater than or equal to 50.")

def validate_record_date(record_date):
    if record_date>timezone.now():
        raise ValidationError("Can't set record in the future.")

def validate_record_broken_date(record_broken_date):
    if record_broken_date < timezone.now():
        raise ValidationError("Can't break record before record was set.")
class SwimRecord(models.Model):
    first_name = models.CharField(max_length=100,validators=[validate_first_name])
    last_name = models.CharField(max_length=100,validators=[validate_last_name])
    team_name = models.CharField(max_length=100,validators=[validate_team_name])
    relay = models.BooleanField(validators=[validate_relay])
    stroke = models.CharField(max_length=100,validators=[validate_stroke])
    distance = models.IntegerField(validators=[validate_distance])
    record_date = models.DateTimeField(validators=[validate_record_date])
    record_broken_date = models.DateTimeField(validators=[validate_record_broken_date])
