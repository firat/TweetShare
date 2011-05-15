from django.db import models
from django.contrib.auth.models import User



class TSProfile(models.Model):
    
    user = models.OneToOneField(User, unique=True)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    twitter_id = models.CharField(max_length=20)
    friends = models.ManyToManyField('self')
    def get_display_name(self):
    	return "%s %s" % (self.first_name, self.last_name)
    	
    def get_photo_src(self):
    	#todo 
    	return ""
    	
    def get_requests(self):
    	return FriendRequest.objects.filter(req_to=self.user).filter(approved=0).filter(ignored=0)
    	
    def get_friends(self):
    """
    returns a list of ``User``
    """
    	return User.objects.filter(id__in=self.friends)
    
class Tweet(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=140)
	datetime = models.DateTimeField()
	t_id = models.CharField(max_field = 30)
	
	
class FriendRequest():
	req_from = models.ForeignKey(User)
	req_to = models.ForeignKey(User)
	approved = models.BooleanField()
	ignored = models.BooleanField()
	
	class Meta:
		unique_together = ('req_from','req_to')
