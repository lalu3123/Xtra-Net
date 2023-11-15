from django.db import models


# Create your models here.
class Support_Engineer_tab(models.Model):
    id = models.AutoField(primary_key=True)
    Support_Engineer = models.CharField(max_length=100)

    def __str__(self):
        return self.Support_Engineer


class Issue_Tab(models.Model):
    id = models.AutoField(primary_key=True)
    Issue = models.CharField(max_length=100)

    def __str__(self):
        return self.Issue

class Status_Tab(models.Model):
    id = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=100)

    def __str__(self):
        return self.Status

class ESCALATION_Tab(models.Model):
    id = models.AutoField(primary_key=True)
    ESCALATION = models.CharField(max_length=100)

    def __str__(self):
        return self.ESCALATION

class data_Tab(models.Model):
    id=models.AutoField(primary_key=True)
    Support_Engineer=models.CharField(max_length=100,null=True)
    User_name=models.CharField(max_length=100,null=True)
    phone_no=models.CharField(max_length=15,null=True)
    LCO=models.CharField(max_length=225,null=True)
    Issue=models.CharField(max_length=100,null=True)
    Remark=models.CharField(max_length=225,null=True)
    Status=models.CharField(max_length=100,null=True)
    ESCALATION=models.CharField(max_length=100,null=True)
    ESCALATION_REMARK = models.CharField(max_length=225,null=True)

    def __str__(self):
        return self.User_name

