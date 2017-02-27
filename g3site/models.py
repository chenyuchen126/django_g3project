from django.db import models
from django.utils import timezone
from djangotoolbox.fields import EmbeddedModelField
from djangotoolbox.fields import ListField
from djangotoolbox.fields import DictField
from django.db import IntegrityError
#from .forms import StringListField
from django.utils.encoding import python_2_unicode_compatible

class Address(models.Model):
	name = models.CharField(max_length=200,null=True)
	website = models.CharField(max_length=200,null=True)
	about = models.CharField(max_length=200,null=True)
	lat = models.FloatField(max_length=200,null=True)
	longt = models.FloatField(max_length=200,null=True)
	area = models.CharField(max_length=200,null=True)
	new_img = models.CharField(max_length=200,null=True)
	address = models.CharField(max_length=200,null=True)	 
	phone = models.CharField(max_length=200,null=True)
        category = models.CharField(max_length=200,null=True)
	overall_star_rating = models.FloatField(max_length=200,null=True)		
	fbid = models.CharField(max_length=200,null=True)
	location = EmbeddedModelField('Location',null=True)
	ontime = EmbeddedModelField('Ontime',null=True)
	cover = EmbeddedModelField('Cover',null=True)
	parking = EmbeddedModelField('Parking',null=True)
        
        def __unicode__(self):
		return self.name

class Location(models.Model):
	city = models.CharField(max_length=200,null=True)
	street = models.CharField(max_length=200,null=True)
	latitude = models.FloatField(max_length=200,null=True)
	longitude = models.FloatField(max_length=200,null=True)
	def __unicode__(self):
		return self.street	

class Cover(models.Model):		
	source = models.CharField(max_length=200,null=True)	
	def __unicode__(self):
		return self.source

class Parking(models.Model):		
	lot = models.CharField(max_length=200,null=True)
	valet = models.CharField(max_length=200,null=True)
	street = models.CharField(max_length=200,null=True)
	def __unicode__(self):
		return self.lot
class Ontime(models.Model):
	sat_2_close =models.CharField(max_length=200,null=True)
	sat_1_close =models.CharField(max_length=200,null=True)
	sun_2_open  =models.CharField(max_length=200,null=True)
	tue_2_open  =models.CharField(max_length=200,null=True)
	thu_2_close =models.CharField(max_length=200,null=True)
	mon_1_open  =models.CharField(max_length=200,null=True)
	sat_2_open  =models.CharField(max_length=200,null=True)
	thu_2_open  =models.CharField(max_length=200,null=True)
	mon_2_open  =models.CharField(max_length=200,null=True)
	sun_1_open  =models.CharField(max_length=200,null=True)
	fri_1_open  =models.CharField(max_length=200,null=True)
	tue_1_close =models.CharField(max_length=200,null=True)
	sun_2_close =models.CharField(max_length=200,null=True)
	wed_1_open  =models.CharField(max_length=200,null=True)
	wed_1_close =models.CharField(max_length=200,null=True)
	tue_1_open  =models.CharField(max_length=200,null=True)
	thu_1_close =models.CharField(max_length=200,null=True)
	sun_1_close =models.CharField(max_length=200,null=True)
	mon_2_close =models.CharField(max_length=200,null=True)
	fri_2_close =models.CharField(max_length=200,null=True)
	sat_1_open  =models.CharField(max_length=200,null=True)
	mon_1_close =models.CharField(max_length=200,null=True)
	fri_2_open  =models.CharField(max_length=200,null=True)
	wed_2_open  =models.CharField(max_length=200,null=True)
	tue_2_close =models.CharField(max_length=200,null=True)
	thu_1_open  =models.CharField(max_length=200,null=True)
	wed_2_close =models.CharField(max_length=200,null=True)
	fri_1_close =models.CharField(max_length=200,null=True)
class Travel(models.Model):
	name = models.CharField(max_length=200,null=True)
	website = models.CharField(max_length=200,null=True)
	about = models.CharField(max_length=200,null=True)
        lat = models.FloatField(max_length=200,null=True)
	longt = models.FloatField(max_length=200,null=True)
        area = models.CharField(max_length=200,null=True)
	picUrl = models.CharField(max_length=200,null=True)
	words = models.CharField(max_length=200,null=True)
	address = models.CharField(max_length=200,null=True)	 
	phone = models.CharField(max_length=200,null=True)
	category_fb = models.CharField(max_length=200,null=True)
	category_ming = models.CharField(max_length=200,null=True)
	rating = models.FloatField(max_length=200,null=True)		
	type1 = models.CharField(max_length=200,null=True)
	gid = models.FloatField(max_length=200,null=True)
	recommends = models.CharField(max_length=200,null=True)
	recommends_name = models.CharField(max_length=200,null=True)
        #ontime = EmbeddedModelField('Ontime',null=True)
        def __unicode__(self):
		return self.name

class Recommends(models.Model):
        name = models.CharField(max_length=200,null=True)
        #categories = CategoryField()


class CategoryField(ListField):
    	def formfield(self, **kwargs):
        	return models.Field.formfield(self, StringListField, **kwargs)

class Janet(models.Model):
	name = models.CharField(max_length=200,null=True)
	description = models.CharField(max_length=200,null=True)
	#tags = ListField(null=True)
	tags = models.CharField(max_length=100)
        categories = CategoryField()
	canon_url = models.CharField(max_length=200,null=True)
	fbid = models.CharField(max_length=200,null=True)
	def __unicode__(self):
		return self.name


@python_2_unicode_compatible
class Category(models.Model):
        name = models.CharField(max_length=200,null=True)
        
        def __str__(self):
                return self.name

class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        def publish(self):
            self.publish_date = timezone.now()
            self.save() 
        def __unicode__(self):
            return self.title
