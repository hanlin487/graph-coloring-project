import sys
from graph import *

def CheckProperColoring(G):#\\\DONE
    """
    Return True if no two adjacent vertices in G have like colors, False otherwise.
    """
    for x in G._adj:
        adjList = G._adj[x]
        for y in adjList:
            if G._color[x] == G._color[y]:
                return False
    return True
#end

def usage():
    print("Usage: $ python3 GraphColoring.py <input file> <output file>", file=sys.stderr)
#end

def main():
    if len(sys.argv) != 3:
        usage()
    try:
        infile = open(sys.argv[1])
    except FileNotFoundError:
        sys.stderr.write("[Errno 2] No such file or directory: '{}'\n".format(sys.argv[1]))
        usage()
    outfile = open(sys.argv[2], 'w')
    
    #line reading and writing
    lines = infile.readlines()
    #print(lines)
    
    #making vertices
    vertices = [x for x in range(1, int(lines[0])+1)]
    

    #edge list
    edges = []
    for line in lines[1:]:
        edge = line.split()
        edge = list(map(int, edge))
        edges.append(tuple(edge))
    

    #graph creation
    G = Graph(vertices, edges)
    

    #coloring and writing to out file
    subset = G.Color()
    print(subset)
    f = []
    v = 'vertex'
    print("{} colors used: {}".format(len(subset), subset), file=outfile)
    print("\nvertex    color ", file=outfile)
    print("----------------",file=outfile) #16 spaces

    for v in G.vertices:
        color = G.getColor(v)
        print(" {0:<10} {1:}".format(v, color), file=outfile)

    infile.close()
    outfile.close()
    
#end

if __name__ == "__main__":
    main()
