from django.shortcuts import render

from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import datetime

from .forms import businessForm
from .models import Business
def business_form(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = businessForm(request.POST, request.FILES)

        bus_inst = Business()
        # Check if the form is valid:
        if form.is_valid():
            #bus_inst.name = form.name
            bus_inst.name = request.POST.get("name", "")
            #bus_inst.mission_statement = form.mission_statement
            bus_inst.mission_statement = request.POST.get("mission_statement", "")
            #bus_inst.incorpDate = form.incorpDate
            bus_inst.incorpDate = request.POST.get("incorpDate", "")
            #bus_inst.files = form.files
            bus_inst.files = request.FILES.get("files", "")
            bus_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse(business_form))
    else:
        form = businessForm()

    return render(request, 'businessForm/business_form.html', {'form': form})
    # If this is a GET (or any other method) create the default form.
    #else:
     #   proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
      #  form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    #return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})
