"""
Unit tests for the Board and BoardColumn classes.
"""

import pytest
from agile_flow_simulator import Board, BoardColumn


class TestBoardColumn:
    """Test cases for BoardColumn enum."""

    def test_all_columns_returns_expected_columns(self) -> None:
        """Test that all_columns returns the correct list of columns."""
        columns = BoardColumn.all_columns()
        assert len(columns) == 5
        assert columns[0] == BoardColumn.BACKLOG
        assert columns[1] == BoardColumn.READY_TO_PULL
        assert columns[2] == BoardColumn.IN_PROGRESS
        assert columns[3] == BoardColumn.TESTING
        assert columns[4] == BoardColumn.COMPLETED

    def test_column_values(self) -> None:
        """Test that column enum values match expected strings."""
        assert BoardColumn.BACKLOG.value == "Backlog"
        assert BoardColumn.READY_TO_PULL.value == "Ready to Pull"
        assert BoardColumn.IN_PROGRESS.value == "In-Progress"
        assert BoardColumn.TESTING.value == "Testing"
        assert BoardColumn.COMPLETED.value == "Completed"


class TestBoard:
    """Test cases for Board class."""

    def test_board_initialization_with_defaults(self) -> None:
        """Test that a board initializes with default columns."""
        board = Board()
        assert board.name == "Kanban Board"
        assert len(board.columns) == 5
        assert board.columns[0] == BoardColumn.BACKLOG
        assert board.columns[-1] == BoardColumn.COMPLETED

    def test_board_initialization_with_custom_name(self) -> None:
        """Test board initialization with a custom name."""
        board = Board(name="My Team Board")
        assert board.name == "My Team Board"

    def test_board_initialization_with_custom_columns(self) -> None:
        """Test board initialization with custom columns."""
        custom_columns = [
            BoardColumn.BACKLOG,
            BoardColumn.IN_PROGRESS,
            BoardColumn.COMPLETED,
        ]
        board = Board(columns=custom_columns)
        assert len(board.columns) == 3
        assert board.columns == custom_columns

    def test_board_requires_at_least_one_column(self) -> None:
        """Test that board validation fails with empty columns."""
        with pytest.raises(ValueError, match="at least one column"):
            Board(columns=[])

    def test_get_column_count(self) -> None:
        """Test getting the column count."""
        board = Board()
        assert board.get_column_count() == 5

        custom_board = Board(columns=[BoardColumn.BACKLOG, BoardColumn.COMPLETED])
        assert custom_board.get_column_count() == 2

    def test_get_column_names(self) -> None:
        """Test getting column names."""
        board = Board()
        names = board.get_column_names()
        assert names == [
            "Backlog",
            "Ready to Pull",
            "In-Progress",
            "Testing",
            "Completed",
        ]

    def test_has_column(self) -> None:
        """Test checking if board has a specific column."""
        board = Board(columns=[BoardColumn.BACKLOG, BoardColumn.IN_PROGRESS])
        assert board.has_column(BoardColumn.BACKLOG) is True
        assert board.has_column(BoardColumn.IN_PROGRESS) is True
        assert board.has_column(BoardColumn.TESTING) is False

    def test_get_column_index(self) -> None:
        """Test getting the index of a column."""
        board = Board()
        assert board.get_column_index(BoardColumn.BACKLOG) == 0
        assert board.get_column_index(BoardColumn.IN_PROGRESS) == 2
        assert board.get_column_index(BoardColumn.COMPLETED) == 4

    def test_get_column_index_not_found(self) -> None:
        """Test getting index of a column not on the board."""
        board = Board(columns=[BoardColumn.BACKLOG])
        assert board.get_column_index(BoardColumn.TESTING) is None

    def test_is_first_column(self) -> None:
        """Test checking if a column is the first column."""
        board = Board()
        assert board.is_first_column(BoardColumn.BACKLOG) is True
        assert board.is_first_column(BoardColumn.IN_PROGRESS) is False
        assert board.is_first_column(BoardColumn.COMPLETED) is False

    def test_is_last_column(self) -> None:
        """Test checking if a column is the last column."""
        board = Board()
        assert board.is_last_column(BoardColumn.COMPLETED) is True
        assert board.is_last_column(BoardColumn.IN_PROGRESS) is False
        assert board.is_last_column(BoardColumn.BACKLOG) is False

    def test_get_next_column(self) -> None:
        """Test getting the next column."""
        board = Board()
        assert board.get_next_column(BoardColumn.BACKLOG) == BoardColumn.READY_TO_PULL
        assert board.get_next_column(BoardColumn.IN_PROGRESS) == BoardColumn.TESTING
        assert board.get_next_column(BoardColumn.COMPLETED) is None

    def test_get_previous_column(self) -> None:
        """Test getting the previous column."""
        board = Board()
        assert board.get_previous_column(BoardColumn.COMPLETED) == BoardColumn.TESTING
        assert board.get_previous_column(BoardColumn.IN_PROGRESS) == BoardColumn.READY_TO_PULL
        assert board.get_previous_column(BoardColumn.BACKLOG) is None

    def test_board_repr(self) -> None:
        """Test the board's __repr__ method."""
        board = Board(name="Test Board")
        repr_str = repr(board)
        assert "Test Board" in repr_str
        assert "Backlog" in repr_str
        assert "Completed" in repr_str

    def test_board_str(self) -> None:
        """Test the board's __str__ method."""
        board = Board(name="Test Board")
        str_repr = str(board)
        assert "Test Board" in str_repr
        assert "Backlog" in str_repr
        assert "|" in str_repr  # Column separator

