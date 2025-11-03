class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    pass # Delete this line to implement the Person class


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
    
    pass # Delete this line to implement the SocialNetwork class



# Test your code here
"""
Assignment #9: Build a Social Network
A graph-based implementation of a social networking platform
"""


class Person:
    """
    Represents a person in the social network.
    
    Attributes:
        name (str): The person's name
        friends (list): A list of Person instances this person is connected to
    """
    
    def __init__(self, name):
        """
        Initialize a new Person.
        
        Args:
            name (str): The name of the person
        """
        self.name = name
        self.friends = []
    
    def add_friend(self, friend):
        """
        Add a friend to this person's friends list.
        
        Args:
            friend (Person): The Person object to add as a friend
        """
        if friend not in self.friends:
            self.friends.append(friend)
    
    def __repr__(self):
        """String representation of the Person object."""
        return f"Person('{self.name}')"


class SocialNetwork:
    """
    Represents a social network using a graph structure (adjacency list).
    
    Attributes:
        people (dict): Dictionary where keys are names and values are Person instances
    """
    
    def __init__(self):
        """Initialize an empty social network."""
        self.people = {}
    
    def add_person(self, name):
        """
        Create a new Person and add them to the network.
        
        Args:
            name (str): The name of the person to add
        """
        if name not in self.people:
            self.people[name] = Person(name)
            print(f"Added {name} to the network.")
        else:
            print(f"{name} already exists in the network.")
    
    def add_friendship(self, person1_name, person2_name):
        """
        Establish a bidirectional friendship between two people.
        
        Args:
            person1_name (str): Name of the first person
            person2_name (str): Name of the second person
        """
        # Check if both people exist
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist in the network.")
            return
        
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist in the network.")
            return
        
        # Get the Person objects
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        
        # Add each person to the other's friends list (bidirectional)
        person1.add_friend(person2)
        person2.add_friend(person1)
        
        print(f"Friendship created between {person1_name} and {person2_name}.")
    
    def print_network(self):
        """
        Print the entire network showing each person and their friends.
        """
        print("\n" + "="*50)
        print("SOCIAL NETWORK")
        print("="*50)
        
        if not self.people:
            print("The network is empty.")
            return
        
        for name, person in sorted(self.people.items()):
            friends_names = [friend.name for friend in person.friends]
            if friends_names:
                print(f"{name}: {', '.join(sorted(friends_names))}")
            else:
                print(f"{name}: (no friends)")
        
        print("="*50 + "\n")


def main():
    """
    Test the social network with various scenarios.
    """
    # Create a new social network
    network = SocialNetwork()
    
    print("STEP 1: Adding people to the network")
    print("-" * 50)
    # Add at least 6 people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")
    network.add_person("Sam")
    
    print("\n" + "STEP 2: Creating friendships")
    print("-" * 50)
    # Create at least 8 friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")
    network.add_friendship("Sam", "Alex")
    
    # Display the network
    network.print_network()
    
    print("STEP 3: Testing edge cases")
    print("-" * 50)
    
    # Test Case 1: Adding a friendship where one person doesn't exist
    print("\nTest 1: Adding friendship with non-existent person")
    network.add_friendship("Alex", "Johnny")
    
    # Test Case 2: Adding duplicate people
    print("\nTest 2: Adding duplicate person")
    network.add_person("Alex")
    
    # Test Case 3: Printing network after series of additions
    print("\nTest 3: Adding new person and creating friendship")
    network.add_person("Jamie")
    network.add_friendship("Jamie", "Alex")
    
    # Display final network
    network.print_network()
    
    # Additional statistics
    print("NETWORK STATISTICS")
    print("-" * 50)
    print(f"Total people: {len(network.people)}")
    
    total_friendships = sum(len(person.friends) for person in network.people.values()) // 2
    print(f"Total friendships: {total_friendships}")
    
    # Find person with most friends
    if network.people:
        most_connected = max(network.people.values(), key=lambda p: len(p.friends))
        print(f"Most connected person: {most_connected.name} ({len(most_connected.friends)} friends)")


if __name__ == "__main__":
    main()


"""A
DESIGN MEMO

Why is a graph the right structure to represent a social network?

Graphs are the ideal data structure for representing social networks because they naturally 
model bidirectional relationships between entities. In a social network, people (nodes) are 
connected through friendships (edges), and these connections can exist between any two people 
regardless of hierarchy or ordering. Graphs excel at representing this many-to-many relationship 
pattern where each person can have multiple friends, and those friends can have their own 
interconnected friend groups. The adjacency list implementation using a dictionary of Person 
objects provides efficient O(1) lookup for finding individuals and their connections.

Why wouldn't a list or tree work as well for this?

A simple list would only store people sequentially but wouldn't capture the relationships 
between them without significant additional complexity. Trees impose a hierarchical parent-child 
structure where each node has one parent, which doesn't reflect the reality of social networks 
where friendships are peer-to-peer and non-hierarchical. In a tree, you couldn't represent a 
situation where Alex is friends with both Jordan and Morgan, and Jordan is also friends with 
Morgan – this creates a cycle that trees cannot represent. Social networks require the 
flexibility to model arbitrary connections, cycles, and multiple paths between people.

What performance or structural trade-offs did you notice when adding friends or printing the network?

Adding a person to the network is O(1) since we're inserting into a dictionary. Creating a 
friendship requires two operations – adding each person to the other's friends list – which is 
O(1) for each addition. However, printing the entire network is O(V + E) where V is the number 
of people and E is the number of friendships, as we must iterate through all people and their 
connections. The space complexity is also O(V + E) because we store each person and all their 
friendship references. One trade-off is that friendships are stored twice (once in each person's 
friends list), which uses more memory but provides O(1) access to a person's friends without 
needing to search through all connections in the network.
"""