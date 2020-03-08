from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


alpha = RegexValidator(r'^[a-zA-Z]*$',"only alphabet is allowed")

def validate_domainonly_email(value):
    """
    Let's validate the email passed is in the domain "yourdomain.com"
    """
    if not "gmail.com" in value:
        raise ValidationError(_("Sorry, the email submitted is invalid. All emails have to be registered on this domain only"), status='invalid')


def valuelength(value):
    if len(value)<2:
        raise ValidationError(_('Entered Value Must be stronger'))

def highvaluelength(value):
    if len(value)<20:
        raise ValidationError(_('Kindly Enter at least 20 or above words'))
