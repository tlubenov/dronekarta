# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    login = models.CharField(max_length=25, verbose_name='Login')
    password = models.CharField(max_length=100, verbose_name='Password')
    phone = models.CharField(max_length=25, verbose_name='Phone number', null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name='Born Date', null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name='Date of last connection', null=True, default=None, blank=True)
    email = models.EmailField(verbose_name='Email')
    years_seniority = models.IntegerField(verbose_name='Seniority', default=0)
    date_created = models.DateTimeField(verbose_name='Date of Birthday', auto_now_add=True)


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=1000, verbose_name='Description')
    client_name = models.CharField(max_length=1000, verbose_name='Client name')


class Supervisor(UserProfile):
    specialization = models.CharField(max_length=50, verbose_name='Specilization')


class Developer(UserProfile):
    supervisor = models.ForeignKey(Supervisor, verbose_name='Supervisor')


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.CharField(max_length=1000, verbose_name='Description')
    time_elapsed = models.IntegerField(verbose_name='Elapsed time',null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name='Importance')
    project = models.ForeignKey(Project, verbose_name='Project',null=True, default=None, blank=True)
    app_user = models.ForeignKey(Developer, verbose_name='User')







