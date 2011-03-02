from django.db import models

# Create your models here.
class News(models.Model):
  news_id = models.AutoField(primary_key=True)
  news_date = models.DateTimeField('date published')
  news_title = models.CharField(max_length=200)
  news_content = models.TextField()
  news_status = models.CharField(max_length=1)
  
  def __unicode__(self):
    return self.news_content
    return self.news_title
    return self.news_date
      
class Page(models.Model):
  page_id = models.CharField(max_length=20,primary_key=True)
  page_name = models.CharField(max_length=200)
  page_title = models.CharField(max_length=75)
  page_key = models.CharField(max_length=120)
  page_desc = models.CharField(max_length=200)
  page_content = models.TextField()
  page_status = models.CharField(max_length=1,default="1")
  
  def __unicode__(self):
    return self.page_id
    return self.page_name
    return self.page_title
    return self.page_key
    return self.page_desc
    #return self.page_contentc/

class MediaFile(models.Model):
  mf_id = models.AutoField(primary_key=True)
  file = models.FileField(upload_to='lib/img')
  mimetype = models.CharField(max_length=64, editable=False)
  created = models.DateTimeField(auto_now_add=True, editable=False)
  updated = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
  def __unicode__(self, *args, **kwargs):
    return u'%s' % self.file.url
  
class DocumentFile(models.Model):
  doc_id = models.AutoField(primary_key=True)
  file = models.FileField(upload_to='lib/doc')
  mimetype = models.CharField(max_length=64, editable=False)
  created = models.DateTimeField(auto_now_add=True, editable=False)
  updated = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
  def __unicode__(self, *args, **kwargs):
    return u'%s' % self.file.url

class CssFile(models.Model):
  css_id = models.AutoField(primary_key=True)
  file = models.FileField(upload_to='lib/doc')
  mimetype = models.CharField(max_length=64, editable=False)
  created = models.DateTimeField(auto_now_add=True, editable=False)
  updated = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
  def __unicode__(self, *args, **kwargs):
    return u'%s' % self.file.url