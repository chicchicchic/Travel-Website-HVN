from src.validators.Regex import Regex


class RegisterCustomerSchema:
    reg_customer_schema = {
        'username': {
            'type': 'string',
            'maxlength': 20,
            'minlength': 5,
            'required': True
        },
        'password': {
            'type': 'string',
            'minlength': 8,
            'maxlength': 20,
            'check_with': Regex.check_regex_password,
            'required': True
        },
        'email': {
            'type': 'string',
            'minlength': 4,
            'check_with': Regex.check_regex_email,
            'required': True
        },
        'phone_number': {
            'type': 'string',
            'minlength': 10,
            'maxlength': 15,
            'check_with': Regex.check_regex_phonenumber,
            'required': True
        },
        'birthday': {
            'type': 'string',
            'minlength': 1,
            'required': True
        },
        'full_name': {
            'type': 'string',
            'maxlength': 100,
            'minlength': 5,
            'required': True
        }
    }
