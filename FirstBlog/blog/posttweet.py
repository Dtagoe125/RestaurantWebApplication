import os
import twitter
import urllib, urllib2
from django.conf import settings
from django.contrib.sites.models import Site
#from models import Food

TWITTER_MAXLENGTH = getattr(settings, 'TWITTER_MAXLENGTH', 140)

def post_to_twitter(sender, instance, *args, **kwargs):
    """ 
    Post new saved objects to Twitter.

    Example:
        from django.db import models

        class MyModel(models.Model):
            text = models.CharField(max_length=255)
            link = models.CharField(max_length=255)

            def __unicode__(self):
                return u'%s' % self.text

            def get_absolute_url(self):
                return self.link

            # the following method is optional
            def get_twitter_message(self):
                return u'my-custom-twitter-message: %s - %s' \
                        % (self.text, self.link)

        models.signals.post_save.connect(post_to_twitter, sender=MyModel)
    """

    # avoid to post the same object twice
    if not kwargs.get('created'):
        return False

    # check if there's a twitter account configured
    try:
        username = settings.TWITTER_USERNAME
        password = settings.TWITTER_PASSWORD
    except AttributeError:
        print 'WARNING: Twitter account not configured.'
        return False

    # if the absolute url wasn't a real absolute url and doesn't contains the
    # protocol and domain defineds, then append this relative url to the domain
    # of the current site, emulating the browser's behaviour
   # url = instance.get_absolute_url()
   # if not url.startswith('http://') and not url.startswith('https://'):
    #    domain = Site.objects.get_current().domain
    #    url = u'http://%s%s' % (domain, url)

    # tinyurl'ze the object's link
    #create_api = 'http://tinyurl.com/api-create.php'
    #data = urllib.urlencode(dict(url=url))
    #link = urllib2.urlopen(create_api, data=data).read().strip()

    # create the twitter message
    try:
        text = instance.get_twitter_message()
    except AttributeError:
        text = unicode(instance)

    mesg = u'%s' % (text)
    if len(mesg) > TWITTER_MAXLENGTH:
        size = len(mesg + '...') - TWITTER_MAXLENGTH
        mesg = u'%s...' % (text[:-size])

    try:
        twitter_api = twitter.Api(username, password)
        twitter_api.PostUpdate(mesg)
    except urllib2.HTTPError, ex:
        print 'ERROR:', str(ex)
        return False