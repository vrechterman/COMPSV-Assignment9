class Person:
    '''
    A class representing a person in a social network.
    
    Attributes:
        name (str): The name of the person.
        friends (list): A list of Person objects who are friends with this person.
    
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends and friend != self:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    
    Attributes:
        people (dict): A dictionary mapping person names (str) to Person objects.
    
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a bidirectional friendship.
        print_network(): Prints each person and their list of friends.
    '''
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people do not exist ({person1_name}, {person2_name}).")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


if __name__ == "__main__":
    network = SocialNetwork()

    for name in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
        network.add_person(name)

    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    network.print_network()

'''
design memo

For this assignment I was tasked to model a social network by using a graph data structure, 
using the graphs I was able to represent the relationships between the people. With that 
being said this system was able to connect, manage, and display the entire network of 
people’s relationships. In the network each person was under a node and or a vertex. 
Then the connection between two nodes is each friendship, which is under an edge, also 
known as a connection. So, for this assignment it is most ideal to use a graph so you 
can represent the social network, because of how naturally it is able to connect one to 
another with friendships. And bidirectional is used so that each friend can have 
many friends, and not just one. For this assignment I also used the adjacency list 
approach because it stores each person as a key, with a list of all the relationships. 
This allows for the system to be faster and more scalable. The main goals for this assignment 
and what I learned was; how to implement a person class, implement a socialnetwork, create
 methods to add a person to the network, bidirectional friendship, print the network. 
 As well as, applying graph theory to real world systems, building object-oriented relationships. 
 
 '''