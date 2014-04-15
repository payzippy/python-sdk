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
