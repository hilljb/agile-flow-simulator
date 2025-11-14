"""
Core Kanban board implementation with columns and state management.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class BoardColumn(str, Enum):
    """Enumeration of valid Kanban board columns."""

    BACKLOG = "Backlog"
    READY_TO_PULL = "Ready to Pull"
    IN_PROGRESS = "In-Progress"
    TESTING = "Testing"
    COMPLETED = "Completed"

    @classmethod
    def all_columns(cls) -> List["BoardColumn"]:
        """Return all board columns in order."""
        return [
            cls.BACKLOG,
            cls.READY_TO_PULL,
            cls.IN_PROGRESS,
            cls.TESTING,
            cls.COMPLETED,
        ]


@dataclass
class Board:
    """
    A Kanban board with configurable columns for managing work items.

    The board maintains an ordered list of columns representing different
    states in an agile workflow.
    """

    columns: List[BoardColumn] = field(default_factory=BoardColumn.all_columns)
    name: str = "Kanban Board"

    def __post_init__(self) -> None:
        """Validate the board after initialization."""
        if not self.columns:
            raise ValueError("Board must have at least one column")

        for col in self.columns:
            if not isinstance(col, BoardColumn):
                raise TypeError(
                    f"Invalid column type: {type(col).__name__}. Must be BoardColumn enum."
                )

    def get_column_count(self) -> int:
        """
        Get the total number of columns on the board.

        Returns:
            The number of columns.
        """
        return len(self.columns)

    def get_column_names(self) -> List[str]:
        """
        Get the names of all columns in order.

        Returns:
            A list of column names as strings.
        """
        return [col.value for col in self.columns]

    def has_column(self, column: BoardColumn) -> bool:
        """
        Check if the board has a specific column.

        Args:
            column: The BoardColumn to check for.

        Returns:
            True if the column exists on the board, False otherwise.
        """
        return column in self.columns

    def get_column_index(self, column: BoardColumn) -> Optional[int]:
        """
        Get the index position of a column on the board.

        Args:
            column: The BoardColumn to find.

        Returns:
            The zero-based index of the column, or None if not found.
        """
        try:
            return self.columns.index(column)
        except ValueError:
            return None

    def is_first_column(self, column: BoardColumn) -> bool:
        """
        Check if a column is the first column on the board.

        Args:
            column: The BoardColumn to check.

        Returns:
            True if this is the first column, False otherwise.
        """
        return self.columns[0] == column if self.columns else False

    def is_last_column(self, column: BoardColumn) -> bool:
        """
        Check if a column is the last column on the board.

        Args:
            column: The BoardColumn to check.

        Returns:
            True if this is the last column, False otherwise.
        """
        return self.columns[-1] == column if self.columns else False

    def get_next_column(self, column: BoardColumn) -> Optional[BoardColumn]:
        """
        Get the next column after the given column.

        Args:
            column: The current BoardColumn.

        Returns:
            The next BoardColumn, or None if this is the last column or column not found.
        """
        index = self.get_column_index(column)
        if index is None or index >= len(self.columns) - 1:
            return None
        return self.columns[index + 1]

    def get_previous_column(self, column: BoardColumn) -> Optional[BoardColumn]:
        """
        Get the previous column before the given column.

        Args:
            column: The current BoardColumn.

        Returns:
            The previous BoardColumn, or None if this is the first column or column not found.
        """
        index = self.get_column_index(column)
        if index is None or index <= 0:
            return None
        return self.columns[index - 1]

    def __repr__(self) -> str:
        """Return a string representation of the board."""
        column_names = " -> ".join(self.get_column_names())
        return f"Board(name='{self.name}', columns=[{column_names}])"

    def __str__(self) -> str:
        """Return a user-friendly string representation of the board."""
        header = f"\n{'='*60}\n{self.name.center(60)}\n{'='*60}\n"
        columns = " | ".join(self.get_column_names())
        return f"{header}{columns}\n{'='*60}"
