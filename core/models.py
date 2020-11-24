from django.db import models
from tinymce import models as tinymce_models

class Committee(models.Model):

    # A committee is a group of commissioners that organises an exec(ut) conference

    name = models.CharField(verbose_name='naam', max_length=300)
    start_year = models.IntegerField(verbose_name='jaartal (begin)')
    end_year = models.IntegerField(verbose_name='jaartal (eind)')
    main_contact_email = models.EmailField(verbose_name='e-mailadres voor contact')
    event_day = models.DateField(verbose_name='datum van het evenement')

    def __str__(self):
        return self.name

class CommissionerRole(models.Model):

    # A commissioner should have role

    name = models.CharField(verbose_name='naam', max_length=300)
    description = models.TextField(verbose_name='omschrijving')

    def __str__(self):
        return self.name

class Commissioner(models.Model):

    # A comissioner is someone who sits in the committee

    committee = models.ManyToManyField(Committee, related_name='commissioners', verbose_name='commissies')
    role = models.ForeignKey(CommissionerRole, on_delete=models.PROTECT)
    first_name = models.CharField(verbose_name='voornaam', max_length=300)
    last_name = models.CharField(verbose_name='achternaam', max_length=300)
    photo = models.FileField(upload_to='commissioners/', verbose_name='foto', null=True, blank=True)
    linkedin_page = models.URLField(verbose_name='linkedin-pagina', max_length=300)
    visible = models.BooleanField(verbose_name='zichtbaar', default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Speaker(models.Model):

    # A speaker is someone who speaks at the conference

    committee = models.ManyToManyField(Committee, related_name='speakers', verbose_name='commissies')
    first_name = models.CharField(verbose_name='voornaam', max_length=300)
    last_name = models.CharField(verbose_name='achternaam', max_length=300)
    short_description = models.TextField(verbose_name='korte omschrijving')
    long_description = tinymce_models.HTMLField(verbose_name='lange omschrijving')
    photo = models.FileField(upload_to='speakers/', verbose_name='foto', null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class SponsorshipTier(models.Model):

    # A sponsorship tier tells us all about how much attention a partner should get

    name = models.CharField(verbose_name='naam', max_length=300)
    css_class = models.CharField(verbose_name='css-class', max_length=300)
    order = models.IntegerField(verbose_name='volgorde', unique=True)

    def __str__(self):
        return self.name

class Sponsor(models.Model):

    # A sponsor so we can show them to the world on our partners-page

    committee = models.ManyToManyField(Committee, related_name='sponsors', verbose_name='commissies')
    name = models.CharField(verbose_name='naam', max_length=300)
    sponsorship_kind = models.ForeignKey(SponsorshipTier, on_delete=models.PROTECT, verbose_name="soort sponsorschap")
    website = models.URLField(verbose_name='website')
    logo = models.FileField(upload_to='sponsors/', verbose_name='logo')

    def __str__(self):
        return self.name


class Activity(models.Model):

    # An activity is an activity on the conference

    ACTIVITY_KINDS = (
        ('talk', 'Talk'),
        ('workshop', 'Workshop'),
        ('break', 'Break')
    )

    activity_kind = models.CharField(choices=ACTIVITY_KINDS, verbose_name="soort activiteit", max_length=300)
    committee = models.ForeignKey(Committee, verbose_name='commissie', on_delete=models.PROTECT)
    name = models.CharField(max_length=300)
    minimum_number_of_people = models.IntegerField(verbose_name='mimum aantal mensen benodigd')
    maximum_number_of_people = models.IntegerField(verbose_name='maximaal aantal mensen toegestaan')
    location = models.CharField(max_length=300)
    commences_at = models.DateTimeField(verbose_name='begint op')
    finishes_at = models.DateTimeField(verbose_name='eindigt op')
    speakers = models.ManyToManyField(Speaker, related_name='activities', verbose_name='sprekers', blank=True)

    def __str__(self):
        return self.name

class Site(models.Model):

    # A site belongs to a committee. The site holds all the meta information about the website of that year's exec(ut) conference.

    name = models.CharField(max_length=300)
    committee = models.ForeignKey(Committee, on_delete=models.PROTECT)
    domain = models.CharField(max_length=300)
    google_tag_manager_id = models.CharField(max_length=300, verbose_name='google tag manager-id')
    logo = models.FileField(upload_to='site_logos/', verbose_name='logo', null=True, blank=True)
    custom_css = models.FileField(upload_to='custom_css/', verbose_name='custom-css', null=True, blank=True)
    description = models.CharField(max_length=300)
    keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.name

