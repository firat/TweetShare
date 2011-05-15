from twitt_share.twitt.models import TS_user
def twitter_id(request):
    if request.method == 'POST': # If the form has been submitted...
	values = request.META.items()
    	values.sort()
    	html = []
    	for k, v in values:
        	html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    	return HttpResponse('<table>%s</table>' % '\n'.join(html))        
	#return HttpResponseRedirect('/mypage/') # Redirect after POST
    else:
	return HttpResponseRedirect('/reg_form_error/') 

def thanks(request):
	return HttpResponse('thanks.html')
