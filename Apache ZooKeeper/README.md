# Apache Zookeeper

## What is it?
ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications.
Consensus algorithm running inside ZooKeeper - ZAB (Zookeeper atomic broadcast)

## Why is it required?
Its uesful to monitor and find out if any node has crashed or not.
- Cluster Support: Management of complete cluster
- Locks in distributed systems
- Configuration management


## Usage (Using the Kazoo Python library)
Zookeeper includes several functions for creating, reading, updating, and deleting Zookeeper nodes (called znodes or nodes here)

### Creating Node
- `ensure_path()` will recursively create the node and any nodes in the path necessary along the way, but can not set the data for the node, only the ACL.
- `create()` creates a node and can set the data on the node along with a watch function. It requires the path to it to exist first, unless the makepath option is set to True.
```
# Ensure a path, create if necessary
zk.ensure_path("/my/favorite")

# Create a node with data
zk.create("/my/favorite/node", b"a value")
```

Ephermeral Node: An ephemeral node will be automatically removed by ZooKeeper when the session associated with the creation of the node expires.
An ephemeral node cannot have children. If the parent node of the given path is ephemeral, a NoChildrenForEphemeralsError will be raised.

### Reading Data
- `exists()` checks to see if a node exists.
- `get()` fetches the data of the node along with detailed node information in a ZnodeStat structure.
- `get_children()` gets a list of the children of a given node.
```
# Determine if a node exists
if zk.exists("/my/favorite"):
    # Do something

# Print the version of a node and its data
data, stat = zk.get("/my/favorite")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

# List the children
children = zk.get_children("/my/favorite")
print("There are %s children with names %s" % (len(children), children))
```

### Updating Data
- `set()` updates the data for a given node. A version for the node can be supplied, which will be required to match before updating the data, or a BadVersionError will be raised instead of updating.
```
zk.set("/my/favorite", b"some data")
```

### Deleting Nodes
- `delete()` deletes a node, and can optionally recursively delete all children of the node as well. A version can be supplied when deleting a node which will be required to match the version of the node before deleting it or a BadVersionError will be raised instead of deleting.
```
zk.delete("/my/favorite/node", recursive=True)
```

### Watchers
Kazoo offers watch functions on a node that gets triggered when a node or its children has changed

Watchers can be set in two different ways
- The first is the style that Zookeeper supports by default for one-time watch events
  ```
  def my_func(event):
    # check to see what the children are now

  # Call my_func when the children change
  children = zk.get_children("/my/favorite/node", watch=my_func)
  ```
- Second is higher level API that watches for data and children modifications, decorators like `ChildrenWatch` and `DataWatch` 
  ```
  @zk.ChildrenWatch("/my/favorite/node")
  def watch_children(children):
      print("Children are now: %s" % children)
  # Above function called immediately, and from then on

  @zk.DataWatch("/my/favorite")
  def watch_node(data, stat):
      print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
  ```

## Data Model
Data stored in a hierarchial namespace, like a file system.
Each node in the namespace is a znode that stores data and can have children.

Types of ZNodes:
- **Persistence:** Alive until they’re explicitly deleted.
- **Ephemeral:** Active until the client connection is alive.
- **Sequential:** Either persistent or ephemeral.

## Usage to Monitor Nodes
The orchestrator creates a `/t` znode. Any parent/child containers that are spawned creates a znode as a child to the `/t`. There is a children watch on the `/t` that is triggered whenever the number of children change.  The watch function either spawns new container or performs leader election based on situation. 

# References
- [ZooKeeper Site](https://zookeeper.apache.org/)
- [Kazoo Library Docs](https://kazoo.readthedocs.io/en/latest/)
- [ZooKeeper Docs](https://cwiki.apache.org/confluence/display/ZOOKEEPER/Index)
- [GFG](https://www.geeksforgeeks.org/what-is-apache-zookeeper/)