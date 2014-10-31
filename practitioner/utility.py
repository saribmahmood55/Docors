'''
from practitioner.models import PractiseTiming
def clinic_timings_dic(query):
	slug_list, mylist, onetime = [], [], []

	for oneClinicSlug in query.iterator():
		slug_list.append(oneClinicSlug.practise_location.slug)

	for oneClinicName in query.iterator():
		mylist.append(oneClinicName.practise_location.name) 

	count = 0
	for clinicname in slug_list:
		dict_timing = []
		for temp_timing in PractiseTiming.pt_objects.practise_timing(clinicname):
			dict_timing.append({'day': temp_timing.day, 'start_time': temp_timing.get_start_time_display(), 'end_time': temp_timing.get_end_time_display()})
		onetime.append({'name':mylist[count], 'timing': dict_timing })
		count += 1
	return onetime
	'''