# Who follows you back on GitHub

## Graph module

Write a class `DirectedGraph`.

__Example:__
```python3
graph = DirectedGraph()
```

### Graph class

The Graph should be:

* Directed
* Unweighted
* Node names should be strings

Don't bother making it more abstract to handle more cases.

There should be the following public methods for the `Graph`:

* `add_edge(node_a, node_b)` - adds an edge between two nodes. If the nodes does not exist, they should be created.
* `get_neighbors_for(node)` - returns a list of nodes (strings) for the given `node`
* `path_between(node_a, node_b)` - returns `true` if there is a path between `nodeA` and `nodeB`. Keep in mind that the graph is directed!
* `__str__` - returns a string representation of the graph. This can be the stringified version of the internal structure of the graph. **Don't draw circles and `-->`**

### Test the Graph class.

Using a library of your choice, make a test-suite to test the `DirectedGraph` class.

Make sure all public methods works just fine - create a test graph and assert that the methods are working.

## Who Follows you back?

We are going to implement a console application, which can give the answer to the fundamental question of the universe - Who follows you back on GitHub?

We want to have the following high-level functionality:

* An app / module that calls the GitHub API and builds a social graph for given users,
* Several HTTP endpoints for querying someone's social graph.

**Since building the social graph can take a long time, think about how to make it more efficient from user's perspective!**


### Implementation details

* Use the [GitHub API](https://developer.github.com/v3/) to fetch an user's followers,
* Make sure to create yourself a GitHub Application from your [Settings panel](https://github.com/settings/applications) and obtain `client_id` and `client_secret`. This is because of API Rate Limiting - https://developer.github.com/v3/rate_limit/
* Make calls with your `client_id` and `client_secret` in order to have `5000` requests per hour!
* Make a module / class that takes a given GitHub username and a **depth of the social graph to build**, which uses the `DirectedGraph` module from the previous task.

Be sure not to build graphs with depth `>= 4` - it's going to take forever ;)

**The class the represents the GitHub social network should have the following methods:**

* `following` - returns a list with the usernames of everyone the user follows,
* `is_following` - accepts an username and returns `True` or `False` depending if the main user follows the one specified by the argument,
* `steps_to` - accepts an username and return the number of hops needed to get to that user following the `following`(pun not quite intended) relation.
