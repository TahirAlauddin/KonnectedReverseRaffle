DATE_FORMAT = "%B %d, %Y"
LICENSE_KEY_VALIDATION_LIMIT = 60 # 60 DAYS = 2 months

LICENSE_KEY_EXPIRED_MESSAGE = F"Cannot use same license key after {LICENSE_KEY_VALIDATION_LIMIT // 30} months and {LICENSE_KEY_VALIDATION_LIMIT%30} days!"
