import random

from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from payzippysdk.ChargingRequest import ChargingRequest
from payzippysdk.ChargingResponse import ChargingResponse
from payzippysdk.QueryRequest import QueryRequest
from payzippysdk.RefundRequest import RefundRequest


def default(request):
    t = get_template('index.html')
    html = t.render(Context())
    return HttpResponse(html)


@csrf_exempt
def refund(request):
    if request.method == 'POST':
        refObj = RefundRequest()
        refObj.set_merchant_transaction_id(request.POST.get('merchant_transaction_id'))
        refObj.set_payzippy_sale_transaction_id(request.POST.get('payzippy_sale_transaction_id'))
        refObj.set_refund_amount(request.POST.get('refund_amount'))
        resObj = refObj.refund()
        print("REFUND:get_response_params", resObj.get_response_params())
        print("REFUND:get_transaction_response", resObj.get_transaction_response().get_transaction_response_params())
        return render_to_response('response/refund_response.html', {'resObj': resObj},
                                  context_instance=RequestContext(request))
    else:
        t = get_template('refund/index.html')
        html = t.render(Context())
        return HttpResponse(html)


@csrf_exempt
def query(request):
    if request.method == 'POST':
        refObj = QueryRequest()
        refObj.set_merchant_key_id(request.POST.get('merchant_key_id'))
        refObj.set_merchant_transaction_id(request.POST.get('merchant_transaction_id'))
        refObj.set_transaction_type(request.POST.get('transaction_type'))
        refObj.set_payzippy_transaction_id(request.POST.get('payzippy_transaction_id'))
        resObj = refObj.query()
        return render_to_response('response/query_response.html', {'resObj': resObj},
                                  context_instance=RequestContext(request))
    else:
        t = get_template('query/index.html')
        html = t.render(Context())
        return HttpResponse(html)


@csrf_exempt
def chargingresponse(request):
    queryStr = request.GET
    resObj = ChargingResponse(queryStr)
    is_valid = resObj.is_valid_response()
    return render_to_response('response/charging_response.html', {'resObj': resObj, 'is_valid': is_valid},
                              context_instance=RequestContext(request))


@csrf_exempt
def chargingmaster(request):
    if request.method == 'POST':
        chObj = ChargingRequest()
        chObj.set_merchant_transaction_id(request.POST.get('merchant_transaction_id'))
        chObj.set_buyer_email_id(request.POST.get('buyer_email_address'))
        chObj.set_transaction_amount(request.POST.get('transaction_amount'))
        chObj.set_payment_method(request.POST.get('payment_method'))
        chObj.set_bank_name(request.POST.get('bank_name'))
        chObj.set_emi_months(request.POST.get('emi_months'))
        chObj.set_ui_mode(request.POST.get('ui_mode'))
        chObj.set_terminal_id(request.POST.get('terminal_id'))
        chObj.set_udf1(request.POST.get('udf1'))
        chObj.set_udf2(request.POST.get('udf2'))
        chObj.set_udf3(request.POST.get('udf3'))
        chObj.set_udf4(request.POST.get('udf4'))
        chObj.set_udf5(request.POST.get('udf5'))
        chObj.set_buyer_phone_no(request.POST.get('buyer_phone_no'))
        chObj.set_buyer_unique_id(request.POST.get('buyer_unique_id'))
        chObj.set_shipping_address(request.POST.get('shipping_address'))
        chObj.set_shipping_city(request.POST.get('shipping_city'))
        chObj.set_shipping_state(request.POST.get('shipping_state'))
        chObj.set_shipping_zip(request.POST.get('shipping_zip'))
        chObj.set_shipping_country(request.POST.get('shipping_country'))
        chObj.set_billing_name(request.POST.get('billing_name'))
        chObj.set_billing_address(request.POST.get('billing_address'))
        chObj.set_billing_city(request.POST.get('billing_city'))
        chObj.set_billing_state(request.POST.get('billing_state'))
        chObj.set_billing_zip(request.POST.get('billing_zip'))
        chObj.set_billing_country(request.POST.get('billing_country'))
        chObj.set_min_sla(request.POST.get('min_sla'))
        chObj.set_is_user_logged_in(request.POST.get('is_user_logged_in'))
        chObj.set_address_count(request.POST.get('address_count'))
        chObj.set_sales_channel(request.POST.get('sales_channel'))
        chObj.set_item_total(request.POST.get('item_total'))
        chObj.set_item_vertical(request.POST.get('item_vertical'))
        chObj.set_sms_notify_number(request.POST.get('sms_notify_number'))
        chObj.set_source(request.POST.get('source'))
        chObj.set_product_info1(request.POST.get('product_info1'))
        chObj.set_product_info2(request.POST.get('product_info2'))
        chObj.set_product_info3(request.POST.get('product_info3'))

        respMap = chObj.charge()

        if respMap["status"] is "OK":
            return render_to_response('charging-master/charging.html', {'obj': respMap},
                                      context_instance=RequestContext(request))
        else:
            html = respMap["error_message"]
            return HttpResponse(html)
    else:
        trxId = str("MT" + str(random.randint(99999999999, 999999999999)))
        t = get_template('charging-master/index.html')
        html = t.render(Context({'trxId': trxId}))
        return HttpResponse(html)


@csrf_exempt
def chargingminimal(request):
    if request.method == 'POST':
        chObj = ChargingRequest()
        chObj.set_merchant_transaction_id(request.POST.get('merchant_transaction_id'))
        chObj.set_buyer_email_id(request.POST.get('buyer_email_address'))
        chObj.set_transaction_amount(request.POST.get('transaction_amount'))
        chObj.set_payment_method(request.POST.get('payment_method'))
        chObj.set_bank_name(request.POST.get('bank_name'))
        chObj.set_emi_months(request.POST.get('emi_months'))
        chObj.set_ui_mode(request.POST.get('ui_mode'))
        respMap = chObj.charge()

        if respMap["status"] is "OK":
            return render_to_response('charging-minimal/charging-minimal.html', {'obj': respMap},
                                      context_instance=RequestContext(request))
        else:
            html = respMap["error_message"]
            return HttpResponse(html)
    else:
        trxId = str("MT" + str(random.randint(99999999999, 999999999999)))
        t = get_template('charging-minimal/index.html')
        html = t.render(Context({'trxId': trxId}))
        return HttpResponse(html)


@csrf_exempt
def chargingredirect(request):
    if request.method == 'POST':
        chObj = ChargingRequest()
        chObj.set_merchant_transaction_id(request.POST.get('merchant_transaction_id'))
        chObj.set_buyer_email_id(request.POST.get('buyer_email_address'))
        chObj.set_transaction_amount(request.POST.get('transaction_amount'))
        chObj.set_payment_method(request.POST.get('payment_method'))
        chObj.set_bank_name(request.POST.get('bank_name'))
        chObj.set_emi_months(request.POST.get('emi_months'))
        chObj.set_ui_mode(request.POST.get('ui_mode'))
        respMap = chObj.charge()
        if respMap["status"] is "OK":
            return render_to_response('charging-redirect/charging-redirect.html', {'obj': respMap},
                                      context_instance=RequestContext(request))
        else:
            html = respMap["error_message"]
            return HttpResponse(html)
    else:
        trxId = str("MT" + str(random.randint(99999999999, 999999999999)))
        t = get_template('charging-redirect/index.html')
        html = t.render(Context({'trxId': trxId}))
        return HttpResponse(html)


@csrf_exempt
def chargingiframe(request):
    if request.method == 'POST':
        chObj = ChargingRequest()
        chObj.set_merchant_transaction_id(request.POST.get('merchant_transaction_id'))
        chObj.set_buyer_email_id(request.POST.get('buyer_email_address'))
        chObj.set_transaction_amount(request.POST.get('transaction_amount'))
        chObj.set_payment_method(request.POST.get('payment_method'))
        chObj.set_bank_name(request.POST.get('bank_name'))
        chObj.set_emi_months(request.POST.get('emi_months'))
        chObj.set_ui_mode(request.POST.get('ui_mode'))
        respMap = chObj.charge()

        if respMap["status"] is "OK":
            return render_to_response('charging-iframe/charging-iframe.html', {'obj': respMap},
                                      context_instance=RequestContext(request))
        else:
            html = respMap["error_message"]
            return HttpResponse(html)
    else:
        trxId = str("MT" + str(random.randint(99999999999, 999999999999)))
        t = get_template('charging-iframe/index.html')
        html = t.render(Context({'trxId': trxId}))
        return HttpResponse(html)