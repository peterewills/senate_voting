# Senate Voting Graphs

This is just a reworking of [previous code]() by [Renzo Lucioni](). Bug fixes have been made, a script for parallel generation of data from each congress 101 through 114 is included, and **Python 3.x is now required.**

A graphs is generated that encodes the pairwise voting affiliations of senators in a given congress. The function `write_graphs(congress)` saves this graph as a `.gexf` file. 

I've also included the `.gexf` files I've generated for my research. Of course, the code can be modified to generate others. However, the format of the paths may change, so you might have to slightly tweak the function `get_senate_vote` if you want to work with older voting records.

## Usage

To write a graph to a `.gexf` file, do

	>> from src import write_graph
	>> write_graph(congress=113)
	
To work directly with the graph, without saving it as a `.gexf`, do

	>> from src import *
	>> import networkx as nx
	>> vote_data = get_all_votes(congress)
	>> G = vote_graph(vote_data)
	>> print(G.nodes())
	
## Credits
 
Author: Peter Wills (peter.e.wills@gmail.com)
 
## License
 
The MIT License (MIT)

Copyright (c) 2017 Peter Wills

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
	
	
	