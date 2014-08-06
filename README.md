===================
Python PayZippy SDK
===================

PayZippy Python SDK provides the interface to use the PayZippy APIs for charging, query and refund.

For the complete usage and examples, please refer the examples given in the SDK

To install the SDK

Extract the file /dist/PayZippySDK-0.1.0.tar.gz by running the command gunzip < PayZippySDK-0.1.0.tar.gz | tar xvf - in your terminal
Go inside the folder PayZippySDK-0.1.0
Run the command python setup.py install in your terminal(Make sure you have python installed in your computer)
To run the examples

Use the examples folder as the template directory in your Django project.
Copy the file config.ini from the directory django/ to your Django project.
Copy the directory static from the directory django/ to your Django project.
Copy the views definition from the file django/views.py to views.py file in your Django project.
Copy the urls definition(including the imports) from the file django/urls.py to urls.py file in your Django project.
Copy the BASE_DIR, STATIC_URL, STATICFILES_DIRS, TEMPLATE_DIRS declarations from the file django/settings.py to settings.py file in your Django project.
To set up your config details, fill the details provided by PayZippy, in config.ini file.
MERCHANT_ID Your Merchant ID
SECRET_KEY Your Secret Key for the Payzippy API. Do not share this!
CALLBACK_URL The URL that the Charging API would call on transaction completion. For the examples provided, this should point to : /chargingresponse as defined in the file urls.py

Sample code snippet to create a charging request object in Django web application is shown below:

```
//In the file views.py
//define a view in the file views.py
//import the charging request object
from payzippysdk.ChargingRequest import ChargingRequest

def chargingrequest(request):
  if request.method == 'POST':
   chObj = ChargingRequest()
   chObj.set_merchant_transaction_id(request.POST.get('merchant_transaction_id'))
   chObj.set_buyer_email_id(request.POST.get('buyer_email_address'))
   chObj.set_transaction_amount(request.POST.get('transaction_amount'))
   chObj.set_payment_method(request.POST.get('payment_method'))
   chObj.set_bank_name(request.POST.get('bank_name'))
   chObj.set_emi_months(request.POST.get('emi_months'))

//The parameters item_vertical,item_total and buyer_phone_no are now mandatory.Pass these parameters for all the transactions(both domestic and international)


//then call charge method which return a dictionary
respMap = chObj.charge()

//validate the status, if OK then render the response, else display the error message
if respMap["status"] is "OK":
  return render_to_response('charging-master/charging.html', {'obj': respMap}, context_instance=RequestContext(request))
else:
  html = respMap["error_message"]
  return HttpResponse(html)

//In the file url.py
//import the views declaration from the above view file in the file url.py
 from <your webapp name>.views import chargingrequest

//map the pattern declaration for chargingrequest, keep the existing mappings as they are
urlpatterns = patterns('',
   url(r'^chargingrequest/$', chargingrequest),
)

//Based on the ui_mode value we can display iframe or redirect
//For integration using IFRAME mode, create a new HTML IFRAME element
//and set its "src" attribute to $charging_object["url"]

{% if obj.params.ui_mode == "IFRAME" %}
   <iframe src="{{ obj.url }}" height="60%" width="100%"></iframe>
{% elif obj.params.ui_mode == "REDIRECT" %}
//For integration using REDIRECT mode, create a new HTML form, with hidden elements.
//Set its "action" attribute to $charging_object["url"].
//Create hidden input elements for every key, value pair in $charging_object["params"]. 
<form method="POST" action="{{ obj.url }}" id="payzippyForm">
{% for key, value in obj.params.items %}
<input type='hidden' name="{{ key }}" value="{{ value }}">
{% endfor %}
</form>

//and then the script to submit the form.
<script>
document.getElementById("payzippyForm").submit();
</script>
```
For complete code sample for the integration you can refer the example and the SDK
