'''
user(phone_number(pkey),age,name,photo_url,date_creation)
group(g_id(pkey),name,date_creation, destination)
group_message(gm_id(pkey),video_url,photo_url,text)
user_is_admin_group(g_id(pkey)(fkey from group),phone_number(fkey from user))
user_is_group_member(g_id(pkey)(fkey from group),phone_number(pkey)(fkey from user))
user_send_group_message(phone_number(pkey)(fkey from user),gm_id(pkey)(fkey from group_message),g_id(fkey from group))
user_receives_group_message(phone_number(pkey)(fkey from user),gm_id(pkey)(fkey from group_message),g_id(fkey from group))
'''

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    phone_number = models.CharField(max_length=10, primary_key=True) #Given by the user
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    photo_url = models.URLField(max_length=100)
    date_creation = models.DateTimeField(default=timezone.now)

class Group(models.Model):
	g_id = models.AutoField(primary_key=True) #Not given by the user, Automatically assigned to user and incremented
	name = models.CharField(max_length=25)
	date_creation = models.DateTimeField(default=timezone.now)
	destination = models.CharField(max_length=50)
	

class Group_message(models.Model):
	gm_id = models.AutoField(primary_key=True) #Not given by the user, Automatically assigned to user and incremented
	video_url = models.URLField(max_length=100)
	photo_url = models.URLField(max_length=100)
	text = models.CharField(max_length=500)


class UserIsAdminGroup(models.Model):
	g_id = models.OneToOneField('group', on_delete=models.CASCADE)
	phone_number = models.OneToOneField('user', on_delete=models.CASCADE)
	
	class Meta:
	    unique_together = ("g_id", "phone_number")

class UserIsGroupMember(models.Model):
	g_id = models.OneToOneField('group', on_delete=models.CASCADE)
	phone_number = models.OneToOneField('user', on_delete=models.CASCADE)
	
	class Meta:
	    unique_together = ("g_id", "phone_number")

class UserSendsGroupMessage(models.Model):
    phone_number = models.OneToOneField('User',on_delete=models.CASCADE)
    gm_id = models.OneToOneField('Group_message',on_delete=models.CASCADE)
    g_id = models.OneToOneField('Group',on_delete=models.CASCADE)
    
    class Meta:
	    unique_together = ("phone_number", "gm_id")

class UserReceivesGroupMessage(models.Model):
    phone_number = models.OneToOneField('User',on_delete=models.CASCADE)
    gm_id = models.OneToOneField('Group_message',on_delete=models.CASCADE)
    g_id = models.OneToOneField('Group',on_delete=models.CASCADE)
    
    class Meta:
	    unique_together = ("phone_number", "gm_id")
