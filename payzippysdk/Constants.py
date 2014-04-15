"""
This file contains the constants needed across in the sdk
"""

VALID_PAYMENT_METHODS = ["CREDIT", "DEBIT", "NET", "EMI", "PAYZIPPY", "CARD_CAPTURE"]
BANK_NAME_REQUIREMENT = ["EMI", "NET"]
UI_MODE_REQUIREMENTS = ["REDIRECT", "IFRAME"]
HASH_METHOD_REQUIREMENTS = ["SHA256", "MD5"]
SALE_REFUND_LIST = ["SALE", "REFUND"]
PAYMENT_MODE_EMI = "EMI"
PAYMENT_MODE_NET = "NET"
PAYMENT_MODE_CARD_CAPTURE = "CARD_CAPTURE"

SUCCESS = "SUCCESS"
ACCEPT = "ACCEPT"
SALE = "SALE"
PARAMS = "params"
URL = "url"
HEADERS = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
POST_METHOD = "POST"
GET_METHOD = "GET"
ERROR = "ERROR"
STATUS = "status"
ERROR_MESSAGE = "error_message"
OK = "OK"

REDIRECT = "REDIRECT"
IFRAME = "IFRAME"
MERCHANT_ID = "merchant_id"
BUYER_EMAIL_ADDRESS = "buyer_email_address"
MERCHANT_TRANSACTION_ID = "merchant_transaction_id"
TRANSACTION_TYPE = "transaction_type"
TRANSACTION_AMOUNT = "transaction_amount"
PAYMENT_METHOD = "payment_method"
BANK_NAME = "bank_name"
EMI_MONTHS = "emi_months"
CURRENCY = "currency"
UI_MODE = "ui_mode"
HASH_METHOD = "hash_method"
HASH = "hash"
MERCHANT_KEY_ID = "merchant_key_id"
BUYER_PHONE_NO = "buyer_phone_no"
BUYER_UNIQUE_ID = "buyer_unique_id"
SHIPPING_ADDRESS = "shipping_address"
SHIPPING_CITY = "shipping_city"
SHIPPING_STATE = "shipping_state"
SHIPPING_ZIP = "shipping_zip"
SHIPPING_COUNTRY = "shipping_country"
SOURCE = "source"
CALLBACK_URL = "callback_url"
BILLING_NAME = "billing_name"
BILLING_ADDRESS = "billing_address"
BILLING_CITY = "billing_city"
BILLING_STATE = "billing_state"
BILLING_ZIP = "billing_zip"
BILLING_COUNTRY = "billing_country"
MIN_SLA = "min_sla"
IS_USER_LOGGED_IN = "is_user_logged_in"
ADDRESS_COUNT = "address_count"
SALES_CHANNEL = "sales_channel"
ITEM_TOTAL = "item_total"
ITEM_VERTICAL = "item_vertical"
TIMEGMT = "timegmt"
UDF1 = "udf1"
UDF2 = "udf2"
UDF3 = "udf3"
UDF4 = "udf4"
UDF5 = "udf5"

CARD_BIN = "card_bin"
CARD_BRAND = "card_brand"
CARD_HASH = "card_hash"
PAYZIPPY_TRANSACTION_ID = "payzippy_transaction_id"
TRANSACTION_STATUS = "transaction_status"
TRANSACTION_RESPONSE_CODE = "transaction_response_code"
TRANSACTION_RESPONSE_MESSAGE = "transaction_response_message"
TRANSACTION_CURRENCY = "transaction_currency"
TRANSACTION_TIME = "transaction_time"
FRAUD_ACTION = "fraud_action"
FRAUD_DETAILS = "fraud_details"
IS_INTERNATIONAL = "is_international"
VERSION = "version"
PAYZIPPY_SALE_TRANSACTION_ID = "payzippy_sale_transaction_id"
REFUND_AMOUNT = "refund_amount"
REFUND_REASON = "refund_reason"
REFUNDED_BY = "refunded_by"
STATUS_CODE = "status_code"
STATUS_MESSAGE = "status_message"
ERROR_CODE = "error_code"
ERROR_MESSAGE = "error_message"
REFUND_STATUS = "refund_status"
REFUND_RESPONSE_CODE = "refund_response_code"
REFUND_RESPONSE_MESSAGE = "refund_response_message"
BANK_ARN = "bank_arn"
TERMINAL_ID = "terminal_id"
BANK_TRANSACTION_ID = "bank_transaction_id"
DATA = "data"
EMI = "emi"
CHARGING_URL = "url"
QUERY_API_HOST = "query_api_host"
QUERY_API_PATH = "query_api_path"
REFUND_API_HOST = "refund_api_host"
REFUND_API_PATH = "refund_api_path"
PRODUCT_INFO1 = "product_info1"
PRODUCT_INFO2 = "product_info2"
PRODUCT_INFO3 = "product_info"
SMS_NOTIFY_NUMBER = "sms_notify_number"
CARD_NUMBER = "card_number"
CREATE_PAYZIPPY_ACCOUNT = "create_payzippy_account"
CVV = "cvv"
EXPIRY_MONTH = "expiry_month"
EXPIRY_YEAR = "expiry_year"
NAME_ON_CARD = "name_on_card"
BANK_NAME_MAXLEN = 100
MERCHANT_ID_MAXLEN = 32
BUYER_EMAIL_ADDRESS_MAXLEN = 100
MERCHANT_TRANSACTION_ID_MAXLEN = 100
MERCHANT_KEY_ID_MAXLEN = 20
BUYER_PHONE_NO_MAXLEN = 50
BUYER_UNIQUE_ID_MAXLEN = 100
SHIPPING_ADDRESS_MAXLEN = 100
SHIPPING_CITY_MAXLEN = 50
SHIPPING_STATE_MAXLEN = 50
SHIPPING_ZIP_MAXLEN = 50
SHIPPING_COUNTRY_MAXLEN = 50
SOURCE_MAXLEN = 20
CALLBACK_URL_MAXLEN = 256
BILLING_NAME_MAXLEN = 255
BILLING_ADDRESS_MAXLEN = 100
BILLING_CITY_MAXLEN = 50
BILLING_STATE_MAXLEN = 50
BILLING_ZIP_MAXLEN = 50
BILLING_COUNTRY_MAXLEN = 50
MIN_SLA_MAXLEN = 100
ADDRESS_COUNT_MAXLEN = 100
SALES_CHANNEL_MAXLEN = 100
ITEM_TOTAL_MAXLEN = 100
ITEM_VERTICAL_MAXLEN = 100
TIMEGMT_MAXLEN = 13
UDF1_MAXLEN = 100
UDF2_MAXLEN = 100
UDF3_MAXLEN = 100
UDF4_MAXLEN = 100
UDF5_MAXLEN = 100
PAYZIPPY_TRANSACTION_ID_MAXLEN = 20
TRANSACTION_STATUS_MAXLEN = 30
TRANSACTION_RESPONSE_CODE_MAXLEN = 30
REFUND_AMOUNT_MAXLEN = 20
REFUNDED_BY_MAXLEN = 100
PAYZIPPY_SALE_TRANSACTION_ID_MAXLEN = 20
REFUND_REASON_MAXLEN = 512
TERMINAL_ID_MAXLEN = 6
TRANSACTION_TYPE_MAXLEN = 20
CARD_NUMBER_MAXLEN = 20
CVV_MAXLEN = 4
EXPIRY_MONTH_MAXLEN = 2
EXPIRY_YEAR_MAXLEN = 4
NAME_ON_CARD_MAXLEN = 100

CARD_NUMBER_INVALID = "CARD NUMBER INVALID"
BANK_NAME_INVALID = "BANK NAME NOT SET"
CURRENCY_INVALID = "CURRENCY NOT SET"
EMAIL_ADDRESS_INVALID = "INVALID EMAIL ADDRESS"
EMI_MONTHS_INVALID = "INVALID EMI MONTHS"
HASH_METHOD_INVALID = "INVALID HASH METHOD"
MERCHANT_ID_INVALID = "INVALID MERCHANT ID"
MERCHANT_KEY_ID_INVALID = "INVALID MERCHANT KEY ID"
MERCHANT_TRANSACTION_ID_INVALID = "INVALID MERCHANT TRANSACTION ID"
PAYMENT_METHOD_INVALID = "INVALID PAYMENT METHOD"
REFUND_AMOUNT_INVALID = "INVALID REFUND AMOUNT"
TRANSACTION_AMOUNT_INVALID = "INVALID TRANSACTION AMOUT"
TRANSACTION_ID_INVALID = "TRANSACTION ID NOT SET"
UI_MODE_INVALID = "INVALID UI MODE"
BUYER_PHONE_NO_INVALID = "INVALID BUYER PHONE NO"
BUYER_UNIQUE_ID_INVALID = "INVALID BUYER UNIQUE ID"
SHIPPING_ADDRESS_INVALID = "INVALID SHIPPING ADDRESS"
SHIPPING_CITY_INVALID = "INVALID SHIPPING CITY"
SHIPPING_STATE_INVALID = "INVALID SHIPPING STATE"
SHIPPING_ZIP_INVALID = "INVALID SHIPPING ZIP"
SHIPPING_COUNTRY_INVALID = "INVALID SHIPPING COUNTRY"
SOURCE_INVALID = "INVALID SOURCE"
CALLBACK_URL_INVALID = "INVALID CALLBACK URL"
BILLING_NAME_INVALID = "INVALID BILLING NAME"
BILLING_ADDRESS_INVALID = "INVALID BILLING ADDRESS"
BILLING_CITY_INVALID = "INVALID BILLING CITY"
BILLING_STATE_INVALID = "INVALID BILLING STATE"
BILLING_ZIP_INVALID = "INVALID BILLING ZIP"
BILLING_COUNTRY_INVALID = "INVALID BILLING COUNTRY"
MIN_SLA_INVALID = "INVALID MIN SLA"
ADDRESS_COUNT_INVALID = "INVALID ADDRESS COUNT"
ITEM_TOTAL_INVALID = "INVALID ITEM TOTAL"
ITEM_VERTICAL_INVALID = "INVALID ITEM VERTICAL"
TIMEGMT_INVALID = "INVALID TIMEGMT"
UDF1_INVALID = "INVALID UDF1"
UDF2_INVALID = "INVALID UDF2"
UDF3_INVALID = "INVALID UDF3"
UDF4_INVALID = "INVALID UDF4"
UDF5_INVALID = "INVALID UDF5"
TERMINAL_ID_INVALID = "INVALID TERMINAL ID"
TRANSACTION_TYPE_INVALID = "INVALID TRANSACTION TYPE"
REFUND_REASON_INVALID = "INVALID REFUND REASON"
REFUNDED_BY_INVALID = "INVALID REFUNDED BY"
IS_USER_LOGGED_IN_INVALID = "USER LOGGED IN INVALID"
SALES_CHANNEL_INVALID = "INVALID SALE CHANNEL"
CVV_INVALID = "INVALID CVV"
EXPIRY_MONTH_INVALID = "INVALID EXPIRY MONTH"
EXPIRY_YEAR_INVALID = "INVALID EXPIRY YEAR"
PAYZIPPY_SALE_TRANSACTION_ID_INVALID = "INVALID PAYZIPPY TRANSACTION ID"