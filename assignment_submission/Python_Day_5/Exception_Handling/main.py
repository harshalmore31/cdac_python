from mypack.voting import Voter, VotingNotAllowedException

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    voter = Voter(name, age)
    print(f"{voter.name} is allowed to vote!")

except VotingNotAllowedException as e:
    print("Exception:", e)
except ValueError:
    print("Please enter a valid number for age.")