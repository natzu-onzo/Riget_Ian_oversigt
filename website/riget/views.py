from django.shortcuts import render, get_object_or_404, redirect
from django.http      import HttpResponse
from django.views     import generic
from django.contrib   import messages
from django.template  import RequestContext
from django.conf      import settings
from django           import forms
from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from django.core.urlresolvers   import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms  import AuthenticationForm
from .models import Fetrecords, Fetpersons
from .forms   import nyFetPerson
from django.db import connection


class loginView(generic.TemplateView):
	tamplate_name = 'registration/login.html'
	tamplate_name_in = 'riget/home.html'

	def get(self, request):
		form = AuthenticationForm(request)
		return render(request, self.tamplate_name, { 'form': form })

#	def post(self, request):
#		return render(request, self.tamplate_name_in, {})

class logoutView(generic.TemplateView):
	tamplate_name = 'riget/base.html'

	def get(self, request):
		return render(request, self.tamplate_name, {})

class homeView(generic.TemplateView):
	tamplate_name = 'riget/home.html'

	def get(self, request):
		return render(request, self.tamplate_name, {})

	def post(self, request):
		return render(request, self.tamplate_name, {})

class fetView(generic.TemplateView):

	tamplate_name = 'riget/fet.html'
	model_0 = Fetrecords
	model_1 = Fetpersons

	def get(self, request):

		if not request.user.is_authenticated():
			return redirect('/')
		cursor = connection.cursor()

		this = Fetrecords.objects.raw('SELECT riget_Fetrecords.*, riget_Fetpersons.firstname, riget_Fetpersons.lastname FROM riget_Fetrecords LEFT JOIN riget_Fetpersons ON riget_Fetpersons.CPR = riget_Fetrecords.CPR')
		print this
		list_r = len(Fetrecords.objects.all())
		list_p = len(Fetpersons.objects.all())

		#fields = ['CPR', 'age', 'scandate', 'scanner', 'tumor_type', 'roi_t_mean_b', 'roi_t_max_b', 'roi_tumor_vol', 'indikation_projekt', 'filter_t', 'MR_DCE']

		return render(request, self.tamplate_name, { 'fetlist':this, 'list_r':list_r, 'list_p':list_p })

		
	
	def post(self, request):
		return render(request, self.tamplate_name, {})

class fetpatientView(generic.TemplateView):
	tamplate_name = 'riget/fetpatient.html'

	def get(self, request, CPR):

		i_person = Fetpersons.objects.raw('SELECT riget_Fetpersons.* FROM riget_Fetpersons WHERE riget_Fetpersons.CPR = "' + str(CPR) + '";')
		i_record = Fetrecords.objects.raw('SELECT riget_Fetrecords.id, riget_Fetrecords.scandato, riget_Fetrecords.age, riget_Fetrecords.scanner, riget_Fetrecords.scantype_type, riget_Fetrecords.tumor_type, riget_Fetrecords.kurveform, riget_Fetrecords.roi_t_mean_b, riget_Fetrecords.roi_t_max_b, riget_Fetrecords.roi_tumor_vol, riget_Fetrecords.indikation_projekt, riget_Fetrecords.interessant_case FROM riget_Fetrecords WHERE riget_Fetrecords.cpr = "' + str(CPR) + '";')
		return render(request, self.tamplate_name, { 'person':i_person, 'records':i_record })

	def post(self, request):
		return render(request, self.tamplate_name, {})


class nyfetrecordView(generic.TemplateView):
	tamplate_name = 'riget/nyfetrecord.html'
	model = Fetrecords

	def get(self, request):
		return render(request, self.tamplate_name, {})

	def post(self, request):
		if request.mothod == "POST":
			form = nyFetRecord(request.POST)

			i_person = Fetpersons.objects.raw('SELECT riget_Fetpersons.id, riget_Fetpersons.firstname, riget_Fetpersons.lastname FROM riget_Fetpersons WHERE riget_Fetpersons.cpr = "' + request.POST['cpr'] + '";')

			u_record = Fetrecords(cpr = request.POST['cpr'],
				firstname = i_person.firstname,
				lastname = i_person.lastname,
				age = request.POST['alder'],
				scandato = request.POST['dato'],
				scanner = request.POST['scanner'],
				scantype_type = request.POST['scan_type'],
				filter_t = request.POST['filter'],
				scantype_pct = request.POST['pct'],
				MR_DCE = request.POST['MR_DCE'],
				MR_DSC = request.POST['MR_DSC'],
				tumor_type = request.POST['tumor_type'],
				kurveform = request.POST['kurveform'],
				indikation_uafklaret_process = request.POST['indikation_uafklaret_process'],
				indikation_gradering = request.POST['indikation_gradering'],
				indikation_biopsioptimering = request.POST['indikation_biopsioptimering'],
				indikation_epi_kir = request.POST['indikation_epi_kir'],
				indikation_praeoperativ_planlaegning = request.POST['indikation_praeoperativ_planlaegning'],
				indikation_rt_planlaegning = request.POST['indikation_rt_planlaegning'],
				indikation_malign_transformation = request.POST['indikation_malign_transformation'],
				indikation_recidiv_straalefoelger = request.POST['indikation_recidiv_straalefoelger'],
				indikation_monitorering = request.POST['indikation_monitorering'],
				indikation_tidlig_postop_vurdering = request.POST['indikation_tidlig_postop_vurdering'],
				indikation_pseudo_progression = request.POST['indikation_pseudo_progression'],
				indikation_projekt = request.POST['indikation_projekt'],
				indikation_andet = request.POST['indikation_andet'],
				roi_b_avg = request.POST['roi_b_avg'],
				roi_suv_threshold = request.POST['roi_suv_threshold'],
				roi_suv_mean = request.POST['roi_suv_threshold'],
				roi_t_mean_b = request.POST['roi_t_mean_b'],
				roi_suv_max = request.POST['roi_suv_max'],
				roi_t_max_b = request.POST['roi_t_max_b'],
				roi_tumor_vol = request.POST['roi_tumor_vol'],
				mr_t1_kontrastop = request.POST['mr_t1_kontrastop'],
				uni_multi_fokal = request.POST['uni_multi_fokal'],
				konklusion_followup = request.POST['konklusion_followup'],
				kbg_ml = request.POST['kbg_ml'],
				interessant_case = request.POST['interessant_case'])

		return render(request, self.tamplate_name, { 'form':form })

class nyfetpersonView(generic.TemplateView):
	tamplate_name = 'riget/nyfetperson.html'
	model = Fetpersons
	fields = ['firstname', 'lastname', 'CPR', 'FDG', 'avastin']

	def get(self, request):
		return render(request, self.tamplate_name, {})

	def post(self, request):
		if request.method == "POST":
			form = nyFetPerson(request.POST)

			u_firstname = request.POST['firstname']
			u_lastname = request.POST['lastname']
			u_CPR = request.POST['CPR']
			u_fdg = request.POST['FDG']
			u_avastin = request.POST['avastin']

			u_person = Fetpersons(CPR = u_CPR,
				firstname = u_firstname,
				lastname = u_lastname,
				FDG = u_fdg,
				avastin = u_avastin,
				lasrChangedBy = "admin")

			u_person.save()

		messages.success(request, "New FET patient oprettet succesfuldt")
		done = "SuccesFuldt oprettet " + str(u_firstname)
		return render(request, self.tamplate_name, { 'form':form, 'done':done }, RequestContext(request))



		return render(request, self.tamplate_name, {})


class changefetpatientView(generic.TemplateView):
	tamplate_name = 'riget/nyfetpersonchange.html'
	model = Fetpersons
	fields = ['firstname', 'lastname', 'CPR', 'FDG', 'avastin']

	def get(self, request, CPR):
		
		i_person = Fetpersons.objects.raw('SELECT riget_Fetpersons.* FROM riget_Fetpersons WHERE riget_Fetpersons.CPR = "' + str(CPR) + '";')
		return render(request, self.tamplate_name, { 'person':i_person })

	def post(self, request, CPR):
		if request.method == "POST":
			form = nyFetPerson(request.POST)

			u_firstname = request.POST['firstname']
			u_lastname = request.POST['lastname']
			u_CPR = request.POST['CPR']
			u_fdg = request.POST['FDG']
			u_avastin = request.POST['avastin']

		i_person = Fetpersons.objects.raw('UPDATE riget_Fetpersons SET CPR="' + str(u_CPR) + '", firstname="' + str(u_firstname) + '", lastname="' + str(u_lastname) + ', FDG="' + str(u_fdg) + ', avastin="' + str(u_avastin) + ' WHERE CPR="' + str(CPR) + '";')

		#t_person.save()


		return render(request, self.tamplate_name, {})


class pibView(generic.TemplateView):
	tamplate_name = 'riget/pib.html'

	def get(self, request):
		return render(request, self.tamplate_name, {})	

























#class Createuser(request):
	
	#user = User.objects.create_user('username', 'firstname', 'lastname', 'password', 'email', 'role', )
