class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        """Initialize a Person with a name and empty friends list."""
        self.name = name
        self.friends = []
    
    def add_friend(self, friend):
        """
        Adds a friend to the person's friend list.
        
        Args:
            friend (Person): The Person object to add as a friend
        """
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        """Initialize an empty social network."""
        self.people = {}
    
    def add_person(self, name):
        """
        Adds a new person to the network.
        
        Args:
            name (str): The name of the person to add
        """
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"Error: {name} already exists in the network.")
    
    def add_friendship(self, person1_name, person2_name):
        """
        Creates a bidirectional friendship between two people.
        
        Args:
            person1_name (str): Name of the first person
            person2_name (str): Name of the second person
        """
        # Check if both people exist in the network
        if person1_name not in self.people:
            print(f"Error: {person1_name} doesn't exist in the network.")
            return
        
        if person2_name not in self.people:
            print(f"Error: {person2_name} doesn't exist in the network.")
            return
        
        # Get Person objects
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        
        # Create bidirectional friendship
        person1.add_friend(person2)
        person2.add_friend(person1)
    
    def print_network(self):
        """Prints the names of all people and their friends."""
        for name in sorted(self.people.keys()):
            person = self.people[name]
            friends_names = ", ".join([friend.name for friend in person.friends])
            print(f"{name} is friends with: {friends_names}")


# Test your code here
if __name__ == "__main__":
    print("=== Testing Person Class ===")
    alex = Person("Alex")
    jordan = Person("Jordan")
    print(f"Alex's friends: {alex.friends}")  # []
    alex.add_friend(jordan)
    print(f"Alex's first friend: {alex.friends[0].name}")  # Jordan
    
    print("\n=== Testing SocialNetwork Class ===")
    network = SocialNetwork()
    
    # Add people (6 people as required)
    network.add_person("Alex")
    network.add_person("Jordan") 
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")
    
    # Create friendships (8+ friendships as required)
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # Test: person doesn't exist
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")
    
    print("\n=== Social Network ===")
    network.print_network()
    
    print("\n=== Testing Edge Cases ===")
    
    # Test duplicate person
    print("\nTest: Adding duplicate person")
    network.add_person("Alex")  # Should show error
    
    # Test non-existent person in friendship
    print("\nTest: Adding friendship with non-existent person")
    network.add_friendship("Riley", "Unknown")  # Should show error
    
    # Test both non-existent people
    print("\nTest: Both people don't exist")
    network.add_friendship("Person1", "Person2")  # Should show error
    
    print("\n=== Final Network State ===")
    network.print_network()

"""
DESIGN MEMO

Why is a graph the right structure to represent a social network?

A graph is the ideal data structure for representing a social network because it naturally 
models relationships between entities. In a graph, people are nodes and friendships are edges, 
which perfectly mirrors real-world social connections. Graphs allow for bidirectional 
relationships (mutual friendships), dynamic connections (adding/removing friends), and complex 
network patterns like mutual friends or friendship chains that would be difficult to represent 
with other structures.

Why wouldn't a list or tree work as well for this?

Lists are linear structures that cannot efficiently represent multi-directional relationships. 
A person can have multiple friends who also have their own friend networks, creating 
interconnected webs that lists cannot capture without significant complexity. Trees impose 
a strict hierarchical parent-child relationship, which doesn't match social networks where 
relationships are peer-to-peer and non-hierarchical. In a tree, each node (except the root) 
has exactly one parent, but in a social network, a person can have any number of friends 
with no hierarchy.

What performance or structural trade-offs did you notice?

Using an adjacency list (dictionary of Person objects with friend lists) provides O(1) lookup 
time for finding a person by name, which is efficient. However, adding friendships requires 
updating both people's friend lists to maintain bidirectionality, which doubles the work. 
The print_network() method has O(n*m) complexity where n is the number of people and m is 
the average number of friends, as it must iterate through all people and their friends. The 
structure prioritizes flexibility and ease of adding connections over memory efficiency, as 
each friendship is stored twice (once for each person).
