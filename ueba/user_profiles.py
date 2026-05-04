class UserProfiles:
    def __init__(self):
        self.profiles = {}

    def update(self, user, metric, value):
        self.profiles.setdefault(user, {})[metric] = value


user_profiles = UserProfiles()
