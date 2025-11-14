"""
Core Kanban board implementation with columns and state management.
"""

from typing import List, Optional
import uuid


DEFAULT_COLUMN_NAMES = ["Backlog", "Ready to Pull", "In Progress", "Testing", "Released"]


class BoardColumn(object):
    """
    A column on a Kanban board.

    Each board column has a name, a randomly generated UUID, an order index, and a list of work items.
    """

    def __init__(self, name: str, order_index: int):
        self.name = name
        self.order_index = order_index
        self.uuid = str(uuid.uuid4())
        self.work_items = []

    def __str__(self) -> str:
        return f"{self.name} (UUID: {self.uuid}, Order: {self.order_index})"

    def __repr__(self) -> str:
        return f"BoardColumn(name='{self.name}', order_index={self.order_index}, uuid='{self.uuid}')"

    def __eq__(self, other) -> bool:
        return self.uuid == other.uuid

    def __lt__(self, other) -> bool:
        return self.order_index < other.order_index

    def __gt__(self, other) -> bool:
        return self.order_index > other.order_index


class Board(object):
    """
    A Kanban board.

    The board maintains an ordered list of columns representing different
    states in an agile workflow.
    """

    def __init__(self, name: str = "Kanban Board", column_names: Optional[List[str]] = None):
        self.name = name

        names_to_create = column_names
        if names_to_create is None or not names_to_create:
            # If no columns are provided or list is empty, create a default set.
            names_to_create = DEFAULT_COLUMN_NAMES

        self.columns = [BoardColumn(name, i) for i, name in enumerate(names_to_create)]
