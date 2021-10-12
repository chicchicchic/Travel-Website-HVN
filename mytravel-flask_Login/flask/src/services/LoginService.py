from src.models.Database import db, login


class LoginService:
    @staticmethod
    def check_login(_username):
        return db.session.query(login.user_id, login.password, login.disable, login.confirm_email) \
            .filter(login.username == _username) \
            .first()
