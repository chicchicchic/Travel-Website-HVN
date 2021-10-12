class LoginSchema:
    login_schema = {
        'username': {
            'type': 'string',
            'maxlength': 20,
            'required': True
        },
        'password': {
            'type': 'string',
            'minlength': 8,
            'required': True
        }
    }
