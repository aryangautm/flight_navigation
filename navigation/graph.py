class Edge:
  """
  Represents an edge in a graph data structure.
  """
  
  def __init__(self, src, dest, label="", weight=0.0):
    """
    Initializes an Edge object.

    Args:
      src (str): The source vertex of the edge.
      dest (str): The destination vertex of the edge.
      label (str, optional): A label associated with the edge. Defaults to "".
      weight (float, optional): A weight associated with the edge. Defaults to 0.0.
    """
    self.src = src
    self.dest = dest
    self.edge_label = label
    self.weight = weight

  def __str__(self):
    """
    Returns a string representation of the edge.

    Returns:
      str: A string representation of the edge including source, destination, weight, and label.
    """
    return f"Airport 1: {self.src} | Airport 2: {self.dest} | Weight: {self.weight} | Edge Label: {self.edge_label}"

  def __lt__(self, other):
    """
    Compares two Edge objects based on their weights.

    Args:
      other (Edge): Another Edge object to compare with.

    Returns:
      bool: True if the calling object's weight is less than the other object's weight, False otherwise.
    """
    return self.weight < other.weight

  def __eq__(self, other):
    """
    Compares two Edge objects based on their source and destination vertices.

    Args:
      other (Edge): Another Edge object to compare with.

    Returns:
      bool: True if the source and destination of both objects are equal, False otherwise.
    """
    return self.src == other.src and self.dest == other.dest
