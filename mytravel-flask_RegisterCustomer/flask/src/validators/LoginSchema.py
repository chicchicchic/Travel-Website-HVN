from src.validators.Regex import Regex

login_schema = {
    'Email': {
        'type': 'string',
        'maxlength': 40,
        'minlength': 5,
        'check_with': Regex.check_regex_email,
        'required': True
    },
    'Password': {
        'type': 'string',
        'minlength': 6,
        'required': True
    }
}
