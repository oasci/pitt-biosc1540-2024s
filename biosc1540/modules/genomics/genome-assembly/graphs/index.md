# Graphs

A graph is a collection of vertices (or nodes) and edges (or links) that connect pairs of vertices.
Graphs can be used to model practically any type of relation by depicting a set of connections among a set of items.
For example, in social networks, vertices could represent individuals, and edges could represent their relationships.

!!! quote "**Figure 1**"

    <figure markdown>
    ![](https://i0.wp.com/sitn.hms.harvard.edu/wp-content/uploads/2021/08/figure1.png){ alight=left width=700 }
    </figure>

    Credit: [Graph Theory 101](https://sitn.hms.harvard.edu/flash/2021/graph-theory-101/).

## Applications

Because graph theory is the study of relationships, it provides a helpful tool for quantifying and simplifying the many moving parts of dynamic systems.
Studying graphs through a framework answers many arrangement, networking, optimization, matching, and operational problems.

Graphs can be used to model many types of relations and processes in physical, biological, social, and information systems, and it has a wide range of valuable applications, such as:

-   Finding communities in networks, such as social media (friend/connection recommendations), or for possible spread of COVID-19 in the community through contacts;
-   Ranking hyperlinks in search engines;
-   GPS in Google Maps to find the shortest path home;
-   Study of molecules and atoms in chemistry;
-   DNA sequencing;
-   Computer network security.

## Fundamentals

A graph, $G$, is a diagram of points and lines connected to the points specified by vertices, $V$, and edges, $E$.

$$
G = (V, E)
$$

It has at least one line joining a set of two vertices with no vertex connecting itself.
The concept of graphs in graph theory stands up on some basic terms such as point, line, vertex, edge, degree of vertices, properties of graphs, etc.

!!! quote "**Figure 2**"

    <figure markdown>
    ![](https://www.tutorialspoint.com/discrete_mathematics/images/graph.jpg){ alight=left width=500 }
    </figure>

    Credit: [tutorialspoint](https://www.tutorialspoint.com/edges-and-vertices-of-graph).

### Vertex

In a graph theory context, a vertex (also called a node) is one of the fundamental units used to construct graphs. Graphs are abstract representations of a set of objects where some pairs of the objects are connected by links.
For instance, vertices in a social network graph could represent people, while in a transportation network, they might represent stations or airports.
Vertices can have properties or attributes.
For example, in a graph modeling a road network, a vertex could have attributes like the name of the location it represents and its geographic coordinates.
In Figure 2, this would be $a$, $b$, $c$ and $d$.

### Edges

In graph theory, an edge is a fundamental component that represents a connection or relationship between two vertices (or nodes) in a graph.
Edges are the links that pair vertices in the graph, forming the graph's structure by indicating how vertices are interconnected.
For example, in Figure 1 our edges would be $\{a, b\}$, $\{a, c\}$, $\{b, c\}$, $\{c, d\}$.

In some graphs, edges have weights or costs associated with them, which can represent distances, capacities, or other quantities depending on the context of the graph.
These are known as weighted graphs.
The weight of an edge can affect the computation of the shortest path, minimum spanning tree, and other graph algorithms.

Depending on the type of graph and the rules applied to it, graphs can have multiple edges (parallel edges) between the same set of vertices and edges that connect a vertex to itself (loops).

## Directionality

There are two main types of graphs, differentiated by the nature of the relationships they model: undirected and directed graphs.

### Undirected

Undirected graphs are a fundamental concept in graph theory.
They serve as a versatile tool for modeling relationships where direction is not a factor.
These graphs consist of vertices and edges, where each vertex represents an entity or object, and each edge signifies a relationship between these entities.
The defining characteristic of undirected graphs is the nature of these edges; they indicate a bidirectional relationship between vertices.
This means the relationship is mutual and does not favor a particular direction.
An edge in an undirected graph serves as a two-way connection, symbolizing that the interaction or connection it represents is reciprocally accessible from either vertex it connects.

!!! quote "**Figure 2**"

    <figure markdown>
    ![](https://www.baeldung.com/wp-content/uploads/sites/4/2020/06/network1-1.png){ alight=left width=500 }
    </figure>

    Credit: [Baeldung](https://www.baeldung.com/cs/graphs-directed-vs-undirected-graph).

Undirected graphs can be found in social network analysis, where vertices correspond to individuals within the network, and edges represent their friendships.
In this context, when an edge connects two vertices, it denotes a mutual friendship between the two individuals.
This mutual aspect is crucial because it implies that the friendship is acknowledged and maintained from both ends without any inherent directionality.
Unlike directed edges, which would imply a specific orientation from a sender to a receiver, the edges in an undirected graph merely connect, signifying that the relationship—like friendship in social networks—is shared equally between both parties.

This characteristic of undirected graphs makes them particularly useful for modeling networks where relationships are inherently non-hierarchical and symmetric, allowing for an intuitive representation of complex systems where the focus is on the presence of a relationship rather than its direction.
By abstracting entities into vertices and their relationships into edges without direction, undirected graphs offer a simplified yet robust framework for analyzing and understanding the structure and dynamics of various interconnected systems.

## Directed

Directed graphs, also known as digraphs, extend the concept of graph theory by introducing directionality to the relationships between entities or objects, represented as vertices.
Just like in undirected graphs, the vertices in directed graphs symbolize entities or objects. However, the key distinction lies in the edges.
In directed graphs, edges are equipped with a direction, typically denoted by an arrow that points from one vertex to another.
This directional arrow transforms the edge into a representation of a one-way relationship, signifying that the interaction or connection it embodies originates from the source vertex and is directed towards the target vertex without implying any reverse relationship.

!!! quote "**Figure 3**"

    <figure markdown>
    ![](https://www.baeldung.com/wp-content/uploads/sites/4/2020/06/network4-2.png){ alight=left width=500 }
    </figure>

    Credit: [Baeldung](https://www.baeldung.com/cs/graphs-directed-vs-undirected-graph).

The introduction of direction to the edges enables directed graphs to model complex systems with asymmetric relationships.
A prime example of this can be seen in web graphs, which represent the structure of the internet.
In such graphs, vertices correspond to web pages, and directed edges symbolize hyperlinks connecting one page.
Here, a directed edge from Page A (the source) to Page B (the target) represents a hyperlink from A to B.
This directed edge indicates that while Page A links to Page B, the converse is not necessarily true.
Page B does not automatically link back to Page A.
This lack of reciprocal implication distinguishes directed from undirected graphs.
It allows for accurately modeling non-mutual relationships across various domains, from web structures and social media influence networks to ecological food webs and beyond.

By incorporating directionality, directed graphs offer a nuanced framework for analyzing directional interactions, flows, or dependencies, providing valuable insights into the directional dynamics of complex systems.
