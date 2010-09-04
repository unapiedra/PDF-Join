from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf

from pdfjoin.forms import *

from pyPdf import PdfFileReader, PdfFileWriter

#@csrf_protect
def show_start(request):
	'''Shows a start page for PDF-Join. '''
	if request.method == 'POST':
		form = FileGroupForm(request.POST, request.FILES)
		if form.is_valid():
			
			import StringIO
			output = PdfFileWriter()
			for name in request.FILES:
				upload = request.FILES[name]
				infile = StringIO.StringIO()
				infile.write(upload.read())
				pdf = PdfFileReader(infile)
				for page in pdf.pages:
					output.addPage(page)
			
			# Set filename
			filename = request.POST['title']
			filename = filename.split('.')[0] + '.pdf'
			
			response = HttpResponse(mimetype="application/pdf")
			response['Content-Disposition'] = 'attachment; filename=%s' % filename
			
			output.write(response)
			infile.close()
			return response
	else:
		form = FileGroupForm()
	return render_to_response('pdfjoin/start.html', {'form': form }, context_instance=RequestContext(request))
