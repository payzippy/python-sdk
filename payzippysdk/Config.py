import ConfigParser

config = ConfigParser.ConfigParser()
config.read("./config.ini")
merchant_section = "MerchantConfig"
merchant_id = config.get(merchant_section, 'MERCHANT_ID')
merchant_key_id = config.get(merchant_section, 'MERCHANT_KEY_ID')
callback_url = config.get(merchant_section, 'CALLBACK_URL')
secret_key = config.get(merchant_section, 'SECRET_KEY')
charging_url = config.get(merchant_section, 'CHARGING_URL')
query_url_host = config.get(merchant_section, 'QUERY_URL_HOST')
query_url_path = config.get(merchant_section, 'QUERY_URL_PATH')
refund_url_host = config.get(merchant_section, 'REFUND_URL_HOST')
refund_url_path = config.get(merchant_section, 'REFUND_URL_PATH')
sale_transaction_type = config.get(merchant_section, 'SALE_TRANSACTION_TYPE')
currency = config.get(merchant_section, 'CURRENCY')
ui_mode = config.get(merchant_section, 'UI_MODE')
hash_method = config.get(merchant_section, 'HASH_METHOD')
blacklist_params = config.get(merchant_section, 'BLACKLISTED_PARAMS')
