import json
from itertools import combinations

import requests
import networkx as nx


def get_senate_vote(vote,congress,year):
    # Year can be replaced to fetch votes from different years (e.g., 2013). 1989 is used
    # as an example.
    url = "https://www.govtrack.us/data/congress/{}/votes/{}/s{}/data.json".format(congress,year,vote)
    page = requests.get(url).text
    try:
        data = json.loads(page)
        return data
    except ValueError:
        raise Exception("Not a valid vote number.")


def get_all_votes(congress):
    vote_num = 1
    vote_dicts = []
    start = 1787 + 2*congress # for example, 101 congress starts in 1989
    for year in [start,start+1]:
        while True:
            try:
                vote_dict = get_senate_vote(vote_num,congress,year)
                vote_dicts.append(vote_dict)
                vote_num += 1
            except Exception:
                break
    return vote_dicts


def vote_graph(data):
    graph = nx.Graph()
    # Set to contain all senator display names - these will be our nodes
    all_senators = set()
    # List to contain roll_call dicts, one for each vote
    roll_calls = []
    for vote in data:
        # Dict with keys for each vote class; values are lists of senator display names
        roll_call = {}
        for key, value in vote['votes'].items():
            senators = []
            for senator in value:
                if senator == 'VP':
                    continue
                senators.append(senator['display_name'])

            roll_call[key] = senators
            # Add any new senators to the set
            all_senators.update(senators)
        roll_calls.append(roll_call)
    
    # All combinations of 2 senator display names
    all_senator_pairs = combinations(all_senators, 2)
    common_votes = {}
    for pair in all_senator_pairs:
        common_votes[pair] = 0
        
    for vote in roll_calls:
        try:
            yea_pairs = combinations(vote['Yea'], 2)
            nay_pairs = combinations(vote['Nay'], 2)
        except KeyError:
            yea_pairs = combinations(vote['Guilty'], 2)
            nay_pairs = combinations(vote['Not Guilty'], 2)
            
        for pair in yea_pairs:
            try:
                common_votes[pair] += 1
            except KeyError:
                # Flip senator names so we can find the pair in the common_votes db
                common_votes[(pair[1],pair[0])] += 1
            
        for pair in nay_pairs:
            try:
                common_votes[pair] += 1
            except KeyError:
                common_votes[(pair[1],pair[0])] += 1
    
    for senator in all_senators:
        party = senator.split()[1][1]
        # Use color names that Graphviz understands
        if party == 'D':
            graph.add_node(senator, color='blue')
        elif party == 'R':
            graph.add_node(senator, color='red')
        else:
            graph.add_node(senator, color='black')

    for pair, votes in common_votes.items():
        # Don't draw an edge for senators with 0 votes in common
        if votes == 0:
            continue
        graph.add_edge(pair[0], pair[1], weight=votes, difference=1.0/votes)

    return graph

def write_graph(congress,directory=''):
    vote_data = get_all_votes(congress)
    G = vote_graph(vote_data)
    path = os.path.join(directory,'votes_{}.gexf'.format(congress))
    nx.write_gexf(G,path)