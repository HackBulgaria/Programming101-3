import sys
from random import shuffle


def make_teams(people, group_size=2):
    result = []
    shuffle(people)

    while len(people) != 0:
        group = people[:group_size]
        result.append(tuple(group))
        people = people[group_size:]

    return result


def main():
    people = ["Rado", "Ivo"]
    
    with open("people", "r") as f:
        people = f.read().split("\n")
        people = [person.strip() for person in people if person.strip() != ""]
    
    for team in make_teams(people):
        m1, m2 = team
        print("{} + {} = team!".format(m1, m2))



if __name__ == "__main__":
    main()
