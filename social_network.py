#-------------------------------------------------------------------------------
# Name:        Gaming Social Network
# Purpose:      CS101 Final project
#
# Author:      Akshay
#
# Created:     21-05-2015
#-------------------------------------------------------------------------------


example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.\
Samson is connected to John.\
Samson likes to play The Legend of Corgi, POKEMON, Dinosaur Diner, DIGIMON, FIRE EMBLEM.\
Karl is connected to Freda.\
Karl likes to play AZUMARILL, The Legend of Corgi, GARCHOMP, Dinosaur Diner, The Movie: The Game, LIFE ORB."

def create_data_structure(string_input):
    """
    Parse a block of text (such as the one above) and store relevant
    information into a data structure.

    Keyword arguments:
        string_input: block of text containing the network information

    Return:
        network data structure, a dictionary.
    """
    network = {}
    for line in string_input.strip().split('.'):
        current = line.strip()
        first_space = current.find(' ')
        name = current[:first_space]
        if line.find('likes to play', first_space) != -1:
            #likes
            likes_start = line.find('likes to play', first_space)
            likes = line[likes_start + len('likes to play'):]
            likes = likes.strip()
            list_of_likes = likes.split(', ')
            if name in network:
                network[name][1] = list_of_likes
            else:
                network[name] = [[],list_of_likes]
        elif line.find('connected to', first_space) != -1:
            conn_start = line.find('connected to ', first_space)
            friends = line[conn_start + len('connected to'):]
            friends = friends.strip()
            list_of_friends = friends.split(', ')
            for e in list_of_friends:
                e = e.strip()
            if name in network:
                network[name][0] = list_of_friends
            else:
                network[name] = [list_of_friends, []]
        else:
            pass

    return network



def get_connections(network, user):
	return network[user][0] if user in network else None


def get_games_liked(network, user):
    return network[user][1] if user in network else None

def add_connection(network, user_A, user_B):
    if (user_A not in network) or (user_B not in network):
        return False
    if user_B in network[user_A][0]:
        return network
    network[user_A][0].append(user_B)
    return network


def add_new_user(network, user, games):
    if user not in network:
        network[user] = [[],games]
    return network


def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)



def get_secondary_connections(network, user):
    connections = []
    if user not in network:
        return None
    c = get_connections(network,user)
    for e in c:
        union(connections,get_connections(network,e))
    return connections


# -----------------------------------------------------------------------------
# connections_in_common(network, user_A, user_B):
#   Finds the number of people that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
# -----------------------------------------------------------------------------
def connections_in_common(network, user_A, user_B):
    if user_A not in network:
        return False
    if user_B not in network:
        return False
    s1 = get_connections(network, user_A)
    s2 = get_connections(network, user_B)
    s3 = []
    for e in s2:
        if e in s1:
            s3.append(e)
    return len(s3)
# -----------------------------------------------------------------------------
# path_to_friend(network, user_A, user_B):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
# -----------------------------------------------------------------------------


def path_to_friend(network, user_A, user_B, visited = None):

    if visited is None:
        visited = {}
    visited[user_A] = True
    connection_list = get_connections(network, user_A)
    if connection_list == None:
        return None
    if user_B in connection_list:
        return [user_A, user_B]
    for node in connection_list:
        if node not in visited:
            temp = path_to_friend(network, node, user_B, visited)
            if temp is not None:
                return [user_A] + temp
    return None

def difference(p, q):
    r = []
    for e in p:
        if e not in q:
            r.append(e)
    return r

def intersection(p, q):
    r = []
    for e in q:
        if e in p:
            r.append(e)

    return r

def quick_sort(p, f):
    if p == []:
        return p

    splitter = p.pop(0)
    lesser = [t for t in p if f(splitter,t)]
    greater = [t for t in p if not f(splitter,t)]
    return quick_sort(lesser, f)+[splitter]+quick_sort(greater, f)

def not_in(p, q):
    for e in p:
        if e[0] == q:
            return False
    return True

def update(p, q, num_times):
    pos = 0
    for i,e in enumerate(p):
        if e[0] == q:
            if e[1] >= num_times:
                return
            else:
                pos = i
                break
    p[pos] = (q,num_times)

def f(p,q):
    return p[1] < q[1]

def get_suggested_games(network, user):
    result = []
    games = get_games_liked(network, user)
    for gamer in network:
        if gamer != user:
            games_liked = get_games_liked(network, gamer)
            num_common = len(intersection(games_liked, games))

            if num_common != len(games_liked) and num_common != 0:

                diff = difference(games_liked, games)
                for e in diff:
                    if not_in(result, e):
                        result.append((e,num_common))
                    else:
                        update(result,e, num_common)

    #sort list based on second element
    result = quick_sort(result, f)
    return [t for (t,p) in result]



def main():
    net = create_data_structure(example_input)
    print get_connections(net, 'Robin')
    print get_secondary_connections(net, "Mercedes")
    print get_suggested_games(net,'John')

if __name__ == '__main__':
    main()
