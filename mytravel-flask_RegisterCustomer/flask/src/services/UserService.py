import uuid
from datetime import datetime

from src.models.Database import db, user_info, login


class UserService:
    @staticmethod
    def register_customer(_username, _password, _fullname, _email, _phone, _birthday):
        try:
            _id = uuid.uuid4()

            _login = login(user_id=str(_id), username=_username, password=_password, disable=False, confirm_email=True,
                           role_id=1001)

            _birthday = datetime.strptime(_birthday, "%Y-%m-%d").strftime("%d-%m-%Y")
            _info = user_info(user_id=str(_id), full_name=_fullname, email=_email, phone_number=_phone,
                              date_create=str(datetime.now()), birthday=_birthday)
            # Multiple insert
            db.session.add_all([_login, _info])
            db.session.commit()
            # return value if commit success is True else if return error
            return True
        except Exception as error:
            db.session.rollback()
            return error.args
