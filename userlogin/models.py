
from django.db import models

from django.core.urlresolvers import reverse



class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    like=models.IntegerField(default=0)



    def __str__(self):
        self.save()
        return self.comment




class Reply(models.Model):
      comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
      reply=models.CharField(max_length=1000,blank=True)



      def __str__(self):
        return self.reply

