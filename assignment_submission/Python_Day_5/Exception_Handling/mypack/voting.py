class VotingNotAllowedException(Exception):
    def __init__(self, message="Age must be 18 or above to vote"):
        super().__init__(message)

class Voter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if age < 18:
            raise VotingNotAllowedException(f"{name} is not allowed to vote (age: {age})")