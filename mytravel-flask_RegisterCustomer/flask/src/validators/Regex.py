import re

regex_email = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
regex_password = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,20}$'
regex_phonenumber = '[0-9\-\+]{9,15}$'
regex_birthday = '/^\d{4}-\d{2}-\d{2}$/'
regex_username = '^\\S*$'


class Regex:
    @staticmethod
    def check_regex_email(field, value, error):
        if not re.match(regex_email, value):
            error(field, 'Value must be type Email')

    @staticmethod
    def check_regex_password(field, value, error):
        if not re.match(regex_password, value):
            error(field, 'Value must be type Password (include Lower Case, Upper Case, Special Characters, Number)')

    @staticmethod
    def check_regex_phonenumber(field, value, error):
        if not re.match(regex_phonenumber, value):
            error(field, 'Value must be type Phone Number')

    @staticmethod
    def check_regex_birthday(field, value, error):
        if not re.match(regex_birthday, value):
            error(field, 'Value must be type date')
            
    @staticmethod
    def check_regex_username(field, value, error):
        if not re.match(regex_username, value):
            error(field, 'Username does not contain a whitespace character')
