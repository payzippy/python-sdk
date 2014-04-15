import urllib
import time

import Constants
from HashUtil import HashUtil
from payzippysdk import Config
import ValidityCheck


class ChargingRequest(object):
    """ ChargingRequest class  contains all the request parameters and the hash generated as per the
    Merchant ID, Merchant Key ID and the key given in the configuration
    """
    def __init__(self):
        self.response = {}
        self.request_params = {}
        self.charging_api_url = Config.charging_url

        self.set_transaction_type(Config.sale_transaction_type)
        self.set_merchant_id(Config.merchant_id)
        self.set_merchant_key_id(Config.merchant_key_id)
        self.set_callback_url(Config.callback_url)
        self.set_currency(Config.currency)
        self.set_ui_mode(Config.ui_mode)
        self.set_hash_method(Config.hash_method)

    # =============================================
    # Mandatory parameters initialized by PZ_Config
    # =============================================

    def set_merchant_id(self, merchant_id):
        self.request_params[Constants.MERCHANT_ID] = merchant_id

    def set_merchant_key_id(self, merchant_key_id):
        self.request_params[Constants.MERCHANT_KEY_ID] = merchant_key_id

    def set_transaction_type(self, transaction_type):
        self.request_params[Constants.TRANSACTION_TYPE] = transaction_type

    def set_ui_mode(self, ui_mode):
        self.request_params[Constants.UI_MODE] = ui_mode

    def set_hash_method(self, hash_method):
        self.request_params[Constants.HASH_METHOD] = hash_method.upper()

    def set_currency(self, currency):
        self.request_params[Constants.CURRENCY] = currency

    def set_callback_url(self, callback_url):
        self.request_params[Constants.CALLBACK_URL] = callback_url

    # ==========================================================
    # Mandatory parameters need to be initialized by Application
    # ==========================================================

    def set_buyer_email_id(self, buyer_email_id):
        self.request_params[Constants.BUYER_EMAIL_ADDRESS] = buyer_email_id

    def set_merchant_transaction_id(self, merchant_transaction_id):
        self.request_params[Constants.MERCHANT_TRANSACTION_ID] = merchant_transaction_id

    def set_transaction_amount(self, transaction_amount):
        self.request_params[Constants.TRANSACTION_AMOUNT] = transaction_amount

    # ===============================================
    # Optional parameters related to merchant details
    # ===============================================

    def set_terminal_id(self, terminal_id):
        self.request_params[Constants.TERMINAL_ID] = terminal_id

    def set_udf1(self, udf1):
        self.request_params[Constants.UDF1] = udf1

    def set_udf2(self, udf2):
        self.request_params[Constants.UDF2] = udf2

    def set_udf3(self, udf3):
        self.request_params[Constants.UDF3] = udf3

    def set_udf4(self, udf4):
        self.request_params[Constants.UDF4] = udf4

    def set_udf5(self, udf5):
        self.request_params[Constants.UDF5] = udf5

    # ============================================
    # Optional parameters related to buyer details
    # ============================================

    def set_buyer_phone_no(self, buyer_phone_no):
        self.request_params[Constants.BUYER_PHONE_NO] = buyer_phone_no

    def set_buyer_unique_id(self, buyer_unique_id):
        self.request_params[Constants.BUYER_UNIQUE_ID] = buyer_unique_id

    def set_shipping_address(self, shipping_address):
        self.request_params[Constants.SHIPPING_ADDRESS] = shipping_address

    def set_shipping_city(self, shipping_city):
        self.request_params[Constants.SHIPPING_CITY] = shipping_city

    def set_shipping_state(self, shipping_state):
        self.request_params[Constants.SHIPPING_STATE] = shipping_state

    def set_shipping_zip(self, shipping_zip):
        self.request_params[Constants.SHIPPING_ZIP] = shipping_zip

    def set_shipping_country(self, shipping_country):
        self.request_params[Constants.SHIPPING_COUNTRY] = shipping_country

    # ==================================================
    # Optional parameters related to transaction details
    # ==================================================

    def set_payment_method(self, payment_method):
        self.request_params[Constants.PAYMENT_METHOD] = payment_method

    def set_emi_months(self, emi_months):
        self.request_params[Constants.EMI_MONTHS] = emi_months

    def set_bank_name(self, bank_name):
        self.request_params[Constants.BANK_NAME] = bank_name

    # ==============================================
    # Optional parameters related to billing details
    # ==============================================

    def set_billing_name(self, billing_name):
        self.request_params[Constants.BILLING_NAME] = billing_name

    def set_billing_address(self, billing_address):
        self.request_params[Constants.BILLING_ADDRESS] = billing_address

    def set_billing_city(self, billing_city):
        self.request_params[Constants.BILLING_CITY] = billing_city

    def set_billing_state(self, billing_state):
        self.request_params[Constants.BILLING_STATE] = billing_state

    def set_billing_zip(self, billing_zip):
        self.request_params[Constants.BILLING_ZIP] = billing_zip

    def set_billing_country(self, billing_country):
        self.request_params[Constants.BILLING_COUNTRY] = billing_country

    # ==============================================
    # Optional parameters useful for fraud detection
    # ==============================================

    def set_min_sla(self, min_sla):
        self.request_params[Constants.MIN_SLA] = min_sla

    def set_is_user_logged_in(self, is_user_logged_in):
        self.request_params[Constants.IS_USER_LOGGED_IN] = is_user_logged_in

    def set_address_count(self, address_count):
        self.request_params[Constants.ADDRESS_COUNT] = address_count

    def set_sales_channel(self, sales_channel):
        self.request_params[Constants.SALES_CHANNEL] = sales_channel

    def set_item_total(self, item_total):
        self.request_params[Constants.ITEM_TOTAL] = item_total

    def set_item_vertical(self, item_vertical):
        self.request_params[Constants.ITEM_VERTICAL] = item_vertical

    def set_sms_notify_number(self, sms_notify_number):
        self.request_params[Constants.SMS_NOTIFY_NUMBER] = sms_notify_number

    # ==================================================
    # Optional parameters related to the product details
    # ==================================================

    def set_source(self, source):
        self.request_params[Constants.SOURCE] = source

    def set_product_info1(self, product_info1):
        self.request_params[Constants.PRODUCT_INFO1] = product_info1

    def set_product_info2(self, product_info2):
        self.request_params[Constants.PRODUCT_INFO2] = product_info2

    def set_product_info3(self, product_info3):
        self.request_params[Constants.PRODUCT_INFO3] = product_info3

    # ============================================================================
    # Card capture parameters, to be used only when payment_method is CARD_CAPTURE
    # ============================================================================

    def set_create_payzippy_account(self, create_payzippy_account):
        self.request_params[Constants.CREATE_PAYZIPPY_ACCOUNT] = create_payzippy_account

    def set_card_number(self, card_number):
        self.request_params[Constants.CARD_NUMBER] = card_number

    def set_cvv(self, cvv):
        self.request_params[Constants.CVV] = cvv

    def set_name_on_card(self, name_on_card):
        self.request_params[Constants.NAME_ON_CARD] = name_on_card

    def set_expiry_month(self, expiry_month):
        self.request_params[Constants.EXPIRY_MONTH] = expiry_month

    def set_expiry_year(self, expiry_year):
        self.request_params[Constants.EXPIRY_YEAR] = expiry_year

    # =================================================
    # Parameters automatically configured during charge
    # =================================================

    def set_timegmt(self):
        self.request_params[Constants.TIMEGMT] = long(round(time.time() * 1000))

    def set_hash(self, hashval):
        self.request_params[Constants.HASH] = hashval

    def get_charging_api_url(self):
        return self.charging_api_url

    # ======================================
    # Charge method, and its helping methods
    # ======================================

    def charge(self):
        try:
            ValidityCheck.validate_charge_params(self.request_params)
        except Exception, e:
            self.response[Constants.STATUS] = Constants.ERROR
            self.response[Constants.ERROR_MESSAGE] = "Invalid parameter : " + str(e)
        else:
            self.set_timegmt()

            hash_util = HashUtil(self.request_params, self.request_params.get(Constants.HASH_METHOD))
            self.request_params[Constants.HASH] = hash_util.generate_hash()

            if self.request_params[Constants.UI_MODE] == Constants.IFRAME:
                url = Config.charging_url + "?" + urllib.urlencode(self.request_params)
            else:
                url = Config.charging_url

            self.response[Constants.PARAMS] = self.request_params
            self.response[Constants.URL] = url
            self.response[Constants.STATUS] = Constants.OK
        return self.response
