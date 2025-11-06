"""
Example usage of the Agile Flow Simulator Board.

This script demonstrates the basic functionality of creating and inspecting
a Kanban board.
"""

from agile_flow_simulator import Board, BoardColumn


def main() -> None:
    """Run example board operations."""
    # Create a board with default settings
    print("Creating a default Kanban board...\n")
    board = Board(name="My Team Board")
    
    # Display the board
    print(board)
    print()
    
    # Show board information
    print(f"Board has {board.get_column_count()} columns:")
    for i, name in enumerate(board.get_column_names(), 1):
        print(f"  {i}. {name}")
    print()
    
    # Demonstrate column navigation
    print("Column Navigation Example:")
    current = BoardColumn.IN_PROGRESS
    print(f"Current column: {current.value}")
    
    prev_col = board.get_previous_column(current)
    if prev_col:
        print(f"Previous column: {prev_col.value}")
    
    next_col = board.get_next_column(current)
    if next_col:
        print(f"Next column: {next_col.value}")
    print()
    
    # Check column positions
    print("Column Position Checks:")
    print(f"Is '{BoardColumn.BACKLOG.value}' the first column? {board.is_first_column(BoardColumn.BACKLOG)}")
    print(f"Is '{BoardColumn.COMPLETED.value}' the last column? {board.is_last_column(BoardColumn.COMPLETED)}")
    print()
    
    # Create a custom board
    print("Creating a simplified board...\n")
    simple_board = Board(
        name="Simple Workflow",
        columns=[
            BoardColumn.BACKLOG,
            BoardColumn.IN_PROGRESS,
            BoardColumn.COMPLETED,
        ]
    )
    print(simple_board)
    print(f"\nThis board has only {simple_board.get_column_count()} columns:")
    print(" -> ".join(simple_board.get_column_names()))


if __name__ == "__main__":
    main()

