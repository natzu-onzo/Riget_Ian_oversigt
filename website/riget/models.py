from __future__ import unicode_literals
from datetime   import date
from django.db  import models

from django.core.urlresolvers import reverse


class Pibpatient(models.Model):
	cpr  = models.CharField(max_length = 15 , null = False)
	fornavn   = models.CharField(max_length = 250, null = False)
	efternavn = models.CharField(max_length = 250, null = False)
	records   = models.CharField(max_length = 250, null = True)

	def __str__(self):
		return str(self.pk)
	def get_absolute_url(self):
		return reverse('riget:login', kwargs={'pk': self.pk})


class Pibrecord(models.Model):
	patient  = models.CharField(max_length = 250, null = True)
	age      = models.CharField(max_length = 250, null = True)
	check1   = models.CharField(max_length = 250, null = True)
	check2   = models.CharField(max_length = 250, null = True)
	check21  = models.CharField(max_length = 250, null = True)
	check22  = models.CharField(max_length = 250, null = True)
	radio22  = models.CharField(max_length = 250, null = True)
	check23  = models.CharField(max_length = 250, null = True)
	check3   = models.CharField(max_length = 250, null = True)
	check31  = models.CharField(max_length = 250, null = True)
	check32  = models.CharField(max_length = 250, null = True)
	check33  = models.CharField(max_length = 250, null = True)
	check34  = models.CharField(max_length = 250, null = True)
	check35  = models.CharField(max_length = 250, null = True)
	check36  = models.CharField(max_length = 250, null = True)
	check37  = models.CharField(max_length = 250, null = True)
	check4   = models.CharField(max_length = 250, null = True)
	check5   = models.CharField(max_length = 250, null = True)
	cerebral = models.CharField(max_length = 250, null = True)
	FDG      = models.CharField(max_length = 250, null = True)
	project  = models.CharField(max_length = 250, null = True)
	date     = models.CharField(max_length = 250, null = True)
	c11      = models.CharField(max_length = 250, null = True)
	PET      = models.CharField(max_length = 250, null = True)
	quality     = models.CharField(max_length = 250, null = True)
	fusioneret  = models.CharField(max_length = 250, null = True)
	fromdate    = models.CharField(max_length = 250, null = True)
	sammenholdt = models.CharField(max_length = 250, null = True)
	HFrontal    = models.CharField(max_length = 250, null = True)
	HPariental  = models.CharField(max_length = 250, null = True)
	HStriatum   = models.CharField(max_length = 250, null = True)
	HOccipital  = models.CharField(max_length = 250, null = True)
	VFrontal    = models.CharField(max_length = 250, null = True)
	VPariental  = models.CharField(max_length = 250, null = True)
	VStriatum   = models.CharField(max_length = 250, null = True)
	VOccipital  = models.CharField(max_length = 250, null = True)
	cerebrum    = models.CharField(max_length = 250, null = True)
	ingen_amyl  = models.CharField(max_length = 250, null = True)
	oeget_amyl  = models.CharField(max_length = 250, null = True)
	konklussion = models.CharField(max_length = 250, null = True)
	intern_t    = models.CharField(max_length = 250, null = True)
	opretter_id = models.CharField(max_length = 250, null = True)
	interessant = models.CharField(max_length = 250, null = True)
	MR_beskrivelse        = models.CharField(max_length = 250, null = True)
	StrukturelSkanning    = models.CharField(max_length = 250, null = True)
	fraStrukturelSkanning = models.CharField(max_length = 250, null = True)

	def __str__(self):
		return str(self.pk)
	def get_absolute_url(self):
		return reverse('riget:login', kwargs={'pk': self.pk})

class Fetpersons(models.Model):
	CPR           = models.CharField(max_length = 128, null= False)
	firstname     = models.CharField(max_length = 250, null= False)
	lastname      = models.CharField(max_length = 250, null= False, default = 'none')
	FDG           = models.BooleanField(default = False, null = False)
	avastin       = models.BooleanField(default = False, null = False)
	lasrChangedBy = models.CharField(max_length = 250, null = False, default = 'admin')

	def __str__(self):
		return str(self.pk) + " " + str(self.CPR) + " " + str(self.firstname)

	def get_absolute_url(self):
		return reverse('riget:login', kwargs={'pk': self.pk})

class Fetpersonsdeleted(models.Model):
	CPR           = models.CharField(max_length = 128, null= False)
	firstename    = models.CharField(max_length = 250, null= False)
	FDG           = models.BooleanField(default = False, null = False)
	avastin       = models.BooleanField(default = False, null = False)
	lasrChangedBy = models.CharField(max_length = 250, null = False, default = 'admin')

	def __str__(self):
		return str(self.pk)

	def get_absolute_url(self):
		return reverse('riget:login', kwargs={'pk': self.pk})

class Fetrecords(models.Model):
	CPR = models.CharField(max_length = 250, null = False)
	age = models.CharField(max_length = 250, null = False)
	scandato = models.DateField(default = date.today, null = False)
	scanner  = models.CharField(max_length = 250, null = False)
	scantype_type = models.CharField(max_length = 250, null = False)
	scantype_pct  = models.CharField(max_length = 250, null = False)
	tumor_type    = models.CharField(max_length = 250, null = False)
	tumor_andet   = models.CharField(max_length = 250, null = False)
	kurveform     = models.CharField(max_length = 250, null = False)
	indikation_uafklaret_process  = models.BooleanField(default = False, null = False)
	indikation_gradering          = models.BooleanField(default = False, null = False)
	indikation_biopsioptimering   = models.BooleanField(default = False, null = False)
	indikation_malign_transformation  = models.BooleanField(default = False, null = False)
	indikation_recidiv_straalefoelger = models.BooleanField(default = False, null = False)
  	indikation_rt_planlaegning         = models.BooleanField(default = False, null = False)
  	indikation_monitorering            = models.BooleanField(default = False, null = False)
  	indikation_tidlig_postop_vurdering = models.BooleanField(default = False, null = False)
  	indikation_epi_kir                   = models.BooleanField(default = False, null = False)
  	indikation_praeoperativ_planlaegning = models.BooleanField(default = False, null = False)
  	indikation_pseudo_progression = models.BooleanField(default = False, null = False)
  	indikation_projekt            = models.CharField(max_length = 250, null = True)
  	indikation_andet              = models.CharField(max_length = 250, null = True)
	roi_b_avg         = models.FloatField(default = 0, null = False)
  	roi_suv_threshold = models.FloatField(default = 0, null = False)
  	roi_suv_mean      = models.FloatField(default = 0, null = False)
  	roi_t_mean_b      = models.FloatField(default = 0, null = False)
  	roi_suv_max       = models.FloatField(default = 0, null = False)
  	roi_t_max_b       = models.FloatField(default = 0, null = False)
  	roi_tumor_vol     = models.FloatField(default = 0, null = False)
	mr_t1_kontrastop  = models.BooleanField(default = False, null = False)
	uni_multi_fokal   = models.CharField(max_length = 250, null = False)
	konklusion_followup = models.CharField(max_length = 250, null = False)
	kommentar = models.CharField(max_length = 250, null = True)
	active    = models.CharField(max_length = 200, null = False)
	kbg_ml    = models.IntegerField(default = 0, null = False)
	interessant_case = models.IntegerField(default = 0, null = False)
	MR_DCE   = models.IntegerField(default = 0, null = False)
	MR_DSC   = models.IntegerField(default = 0, null = False)
	filter_t = models.CharField(max_length = 250, null = True)
	
	def __str__(self):
		return str(self.pk)

	def get_absolute_url(self):
		return reverse('riget:login', kwargs={'pk': self.pk})

class Fetrecordsdeleted(models.Model):
	CPR = models.CharField(max_length = 250, null = False)
	age = models.CharField(max_length = 250, null = False)
	scandato = models.DateField(default = date.today, null = False)
	scanner  = models.CharField(max_length = 250, null = False)
	scantype_type = models.CharField(max_length = 250, null = False)
	scantype_pct  = models.CharField(max_length = 250, null = False)
	tumor_type    = models.CharField(max_length = 250, null = False)
	tumor_andet   = models.CharField(max_length = 250, null = False)
	kurveform     = models.CharField(max_length = 250, null = False)
	indikation_uafklaret_process  = models.BooleanField(default = False, null = False)
	indikation_gradering          = models.BooleanField(default = False, null = False)
	indikation_biopsioptimering   = models.BooleanField(default = False, null = False)
	indikation_malign_transformation  = models.BooleanField(default = False, null = False)
	indikation_recidiv_straalefoelger = models.BooleanField(default = False, null = False)
  	indikation_rt_planlaegning         = models.BooleanField(default = False, null = False)
  	indikation_monitorering            = models.BooleanField(default = False, null = False)
  	indikation_tidlig_postop_vurdering = models.BooleanField(default = False, null = False)
  	indikation_epi_kir                   = models.BooleanField(default = False, null = False)
  	indikation_praeoperativ_planlaegning = models.BooleanField(default = False, null = False)
  	indikation_pseudo_progression = models.BooleanField(default = False, null = False)
  	indikation_projekt            = models.CharField(max_length = 250, null = True)
  	indikation_andet              = models.CharField(max_length = 250, null = True)
	roi_b_avg         = models.FloatField(default = 0, null = False)
  	roi_suv_threshold = models.FloatField(default = 0, null = False)
  	roi_suv_mean      = models.FloatField(default = 0, null = False)
  	roi_t_mean_b      = models.FloatField(default = 0, null = False)
  	roi_suv_max       = models.FloatField(default = 0, null = False)
  	roi_t_max_b       = models.FloatField(default = 0, null = False)
  	roi_tumor_vol     = models.FloatField(default = 0, null = False)
	mr_t1_kontrastop  = models.BooleanField(default = False, null = False)
	uni_multi_fokal   = models.CharField(max_length = 250, null = False)
	konklusion_followup = models.CharField(max_length = 250, null = False)
	kommentar = models.CharField(max_length = 250, null = True)
	active    = models.CharField(max_length = 200, null = False)
	kbg_ml    = models.IntegerField(default = 0, null = False)
	interessant_case = models.IntegerField(default = 0, null = False)
	MR_DCE   = models.IntegerField(default = 0, null = False)
	MR_DSC   = models.IntegerField(default = 0, null = False)
	filter_t = models.CharField(max_length = 250, null = True)

class Fetusers(models.Model):
	username = models.CharField(max_length = 250, null = False)
	md5pass = models.CharField(max_length = 250, null = False)

	def __str__(self):
		return str(self.pk)

	def get_absolute_url(self):
		return reverse('riget:login', kwargs={'pk': self.pk})

class riget_fet_persons(models.Model):
	name = models.CharField(max_length = 200, null = True)
	alder = models.CharField(max_length = 200, null = True)


	def __str__(self):
		return str(self.pk)

class Fetrecordimages(models.Model):
	img = models.CharField(max_length = 250, null = False)
	record = models.IntegerField(default = 0, null = False)
	CPR = models.CharField(max_length = 250, null = False)
	filename = models.CharField(max_length = 250, null = False)
	comment = models.CharField(max_length = 250, null = False)

	def __str__(self):
		return str(self.pk)

	def get_absolute_url(self):
		return reverse('riget:login', kwargs={'pk': self.pk})

class User(models.Model):
	username   = models.CharField(max_length = 250, null = True)
	first_name = models.CharField(max_length = 250, null = True)
	last_name  = models.CharField(max_length = 250, null = True)
	password  = models.CharField(max_length = 250, null = True)
	email     = models.EmailField(max_length = 250, null = True)
	role      = models.CharField(max_length = 250, null = True)
	authenticated = models.CharField(max_length = 250, null = True)
	pibrecords    = models.ManyToManyField(Pibrecord)

	def __str__(self):
		return str(self.pk)
	def get_absolute_url(self):
		return reverse('riget:login', kwargs={'pk': self.pk})


