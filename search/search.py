

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    "*** YOUR CODE HERE ***"
    dfs_stack = util.Stack()  # Use a stack for dfs
    path = []
    path.append(problem.getStartState())
    dfs_stack.push((path, []))

    while not dfs_stack.isEmpty():
        curr_path, actions = dfs_stack.pop()
        end_state = curr_path[-1]
        if problem.isGoalState(end_state):
            return actions
        for successor in problem.getSuccessors(end_state):
            next_state = successor[0]
            # Implement path checking 
            if next_state not in curr_path:
                next_dir = successor[1]
                dfs_stack.push(
                    (curr_path + [next_state], actions + [next_dir]))

    return False
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    bfs_queue = util.Queue()
    visited = []
    bfs_queue.push((problem.getStartState(), []))

    while not bfs_queue.isEmpty():
        state, actions = bfs_queue.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            for successor in problem.getSuccessors(state):
                next_state = successor[0]
                next_dir = successor[1]
                bfs_queue.push((next_state, actions + [next_dir]))

    return False
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ucs_heap = util.PriorityQueue()
    visited = []
    ucs_heap.update((problem.getStartState(), []),
                    problem.getCostOfActions([]))

    while not ucs_heap.isEmpty():
        state, actions = ucs_heap.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            for successor in problem.getSuccessors(state):
                next_state = successor[0]
                next_dir = successor[1]
                next_cost = problem.getCostOfActions(actions + [next_dir])
                ucs_heap.update((next_state, actions + [next_dir]), next_cost)
    return False

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    a_star_heap = util.PriorityQueue()
    visited = []
    a_star_heap.update((problem.getStartState(), []),
                       problem.getCostOfActions([]))

    while not a_star_heap.isEmpty():
        state, actions = a_star_heap.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            for successor in problem.getSuccessors(state):
                next_state = successor[0]
                next_dir = successor[1]
                next_cost = problem.getCostOfActions(actions + [next_dir])
                next_heur = heuristic(next_state, problem)
                a_star_heap.update(
                    (next_state, actions + [next_dir]), next_cost + next_heur)
    return False

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
