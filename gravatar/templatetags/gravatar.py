import urllib

from django import template
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.html import escape
from django.utils.hashcompat import md5_constructor

GRAVATAR_URL_PREFIX = getattr(settings, "GRAVATAR_URL_PREFIX", "http://www.gravatar.com/")
GRAVATAR_DEFAULT_IMAGE = getattr(settings, "GRAVATAR_DEFAULT_IMAGE", "")

def get_user(user):
    if not isinstance(user, User):
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            # TODO: make better? smarter? strong? maybe give it wheaties?
            raise Exception, "Bad user for gravatar."
    return user
    
def gravatar_for_email(email, size=80):
    """
    Returns the url for the gravatar of the passed email address
    """
    
    h = md5_constructor(email.lower()).hexdigest()
    
    url = "%savatar/%s?" % (GRAVATAR_URL_PREFIX, h)
    url += urllib.urlencode({"d": GRAVATAR_DEFAULT_IMAGE})
    
    if not default_is_url():
        # don't bother with size attribute if the custom image is a url
        url += "&" + urllib.urlencode({"s": str(size)})
        
    return escape(url)

def gravatar_for_user(user, size=80):
    """
    Returns the url for the gravatar of the passed username or user instance
    """
    
    user = get_user(user)
    return gravatar_for_email(user.email, size)

def gravatar_img_for_email(email, size=80):
    """
    Returns an img tag for the passed email. No title attribute is affixed
    """
    
    url = gravatar_for_email(email, size)
    return '<img src="%s" %s/>' % (escape(url), size)

def gravatar_img_for_user(user, size=80):
    """
    Returns an img tag for the passed user.
    """
    
    user = get_user(user)
    url = gravatar_for_user(user)    
    size = get_size_for_tag(size)
    title = 'alt="Avatar for %s"' % user
    
    return '<img src="%s" %s %s/>' % (escape(url), title, size)

def get_size_for_tag(size):
    """
    Do not include size attributes to the tag, if the default setting is a url
    """
    
    if default_is_url():
        return ""
    
    return'height="%s" width="%s"' % (size, size)

def default_is_url():
    """
    Determines if the default image setting is a URL
    """
    
    return GRAVATAR_DEFAULT_IMAGE.startswith("http://")

def gravatar(user, size=80):
    return gravatar_img_for_user(user, size)

register = template.Library()
register.simple_tag(gravatar)
register.simple_tag(gravatar_for_user)
register.simple_tag(gravatar_for_email)
register.simple_tag(gravatar_img_for_user)
register.simple_tag(gravatar_img_for_email)
