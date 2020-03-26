from User import User


class UserLibrary:
    def __init__(self):
        self.users = {}

    def get_user(self, username):
        return self.users.get(username)

    def user_exist(self, username):
        return username in self.users

    def add_user(self, username):
        if not(self.user_exist(username)):
            user = User(username)
            self.users[username] = user
            return True
        if not self.users[username].logged_in:
            self.users[username].login()
            return True
        return False

    def logout(self, username):
        user = self.users.get(username)
        user.logout()
