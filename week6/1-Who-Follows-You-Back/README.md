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

### Test the Graph class.

Using Python's `unittest`, make a test-suite to test the `DirectedGraph` class.

Make sure all public methods works just fine - create a test graph and assert that the methods are working.

## Who Follows you back?

We are going to implement a console application, which can give the answer to the fundamental question of the universe -**Who follows you back on GitHub?**

We want to have the following high-level functionality:

* A script that calls the GitHub API and builds a social graph for a given user.
* A console interface to ask questions about that user.

We want to be able to ask the following questions:

1. Do you follow user with username `X`? This is a Yes/No question.
2. Does someone with username `X` follows you? This is a Yes/No question.
3. How many people from your followers follows you back?

### Implementation details

* In order to fetch JSON for a given user you can make call to this API endpoint: [https://api.github.com/users/radorado](https://api.github.com/users/radorado). Just substitute `radorado` with your username.
* Use the [GitHub API](https://developer.github.com/v3/) to fetch an user's followers,
* Make sure to create yourself a GitHub Application from your [Settings panel](https://github.com/settings/applications) and obtain `client_id` and `client_secret`. This is because of API Rate Limiting - https://developer.github.com/v3/rate_limit/
* Make calls with your `client_id` and `client_secret` in order to have `5000` requests per hour!
* Make a class that takes a given GitHub username and a **level of the social graph to build**, which uses the `DirectedGraph` module from the previous task.

Be sure not to build graphs with level `>= 4` - it's going to take forever ;)

**The class the represents the GitHub social network should have the following methods:**

* `do_you_follow(user)` - returns True / False if you follow directly the given `user`,
* `do_you_follow_indirectly(user)` - returns True / False if someone from the people you follow, follows the `user`. Limit your self to the `level` of the graph.
* `does_he_she_follows(user)` - returns True / False if the given `user` follows you directly.
* `does_he_she_follows_indirectly(user)` - returns True / False if the given `users` follows someone who follows you.
* `who_follows_you_back()` - returns a list of usernames, that follows you and are followed by you or by the people you follow (limit yourself to the `level` of the graph)
