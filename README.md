# Agile Flow Simulator

A Python package for modeling Kanban boards and simulating agile team development workflows. This library provides a robust, type-safe implementation of Kanban boards with extensible support for work items, flow metrics, and forecasting.

## Features

- 🎯 **Type-Safe Board Modeling**: Built with modern Python type hints and dataclasses
- 📊 **Standard Kanban Columns**: Pre-configured with typical agile workflow states
- 🔧 **Extensible Design**: Easy to customize columns and extend functionality
- ✅ **Well-Tested**: Comprehensive test coverage with pytest
- 📝 **Clean API**: Intuitive methods for board inspection and navigation

## Requirements

- Python 3.10 or higher

## Installation

### Using Conda (Recommended)

```bash
# Create/update the conda environment
conda env create -f environment.yaml

# Or update existing environment
conda env update -f environment.yaml

# Activate the environment
conda activate agile-flow-metrics

# Install the package in development mode
pip install -e .
```

### Using pip (Alternative)

```bash
pip install -e ".[dev]"
```

## Quick Start

### Creating a Basic Board

```python
from agile_flow_simulator import Board, BoardColumn

# Create a board with default columns
board = Board(name="My Team Board")

# Display the board
print(board)
```

### Working with Board Columns

```python
from agile_flow_simulator import Board, BoardColumn

board = Board()

# Get all column names
column_names = board.get_column_names()
print(column_names)
# Output: ['Backlog', 'Ready to Pull', 'In-Progress', 'Testing', 'Completed']

# Check if board has a specific column
has_testing = board.has_column(BoardColumn.TESTING)
print(f"Has testing column: {has_testing}")  # True

# Get the next column in the workflow
next_col = board.get_next_column(BoardColumn.IN_PROGRESS)
print(next_col)  # BoardColumn.TESTING

# Check column positions
is_first = board.is_first_column(BoardColumn.BACKLOG)  # True
is_last = board.is_last_column(BoardColumn.COMPLETED)  # True
```

### Custom Board Configuration

```python
from agile_flow_simulator import Board, BoardColumn

# Create a simplified board with only specific columns
custom_board = Board(
    name="Simple Workflow",
    columns=[
        BoardColumn.BACKLOG,
        BoardColumn.IN_PROGRESS,
        BoardColumn.COMPLETED,
    ]
)

print(f"Number of columns: {custom_board.get_column_count()}")  # 3
```

## Board Columns

The default Kanban board includes five columns:

1. **Backlog**: Items waiting to be prioritized
2. **Ready to Pull**: Items ready for the team to work on
3. **In-Progress**: Items currently being worked on
4. **Testing**: Items undergoing quality assurance
5. **Completed**: Finished items

## API Reference

### Board Class

#### Properties
- `name`: str - The name of the board
- `columns`: List[BoardColumn] - Ordered list of columns on the board

#### Methods
- `get_column_count()` → int - Returns the number of columns
- `get_column_names()` → List[str] - Returns column names as strings
- `has_column(column)` → bool - Check if a column exists on the board
- `get_column_index(column)` → Optional[int] - Get the position of a column
- `is_first_column(column)` → bool - Check if column is first
- `is_last_column(column)` → bool - Check if column is last
- `get_next_column(column)` → Optional[BoardColumn] - Get the next column
- `get_previous_column(column)` → Optional[BoardColumn] - Get the previous column

### BoardColumn Enum

An enumeration of valid Kanban board columns:
- `BACKLOG`
- `READY_TO_PULL`
- `IN_PROGRESS`
- `TESTING`
- `COMPLETED`

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=agile_flow_simulator --cov-report=html

# Run specific test file
pytest tests/test_board.py
```

### Type Checking

```bash
mypy agile_flow_simulator
```

### Code Formatting

```bash
# Format code
black agile_flow_simulator tests

# Sort imports
isort agile_flow_simulator tests

# Check style
flake8 agile_flow_simulator tests
```

## Roadmap

- ✅ Board structure with typed columns
- 🔄 Work item (card) management
- 🔄 Moving cards between columns
- 🔄 WIP (Work in Progress) limits
- 🔄 Flow metrics (cycle time, throughput, etc.)
- 🔄 Monte Carlo forecasting
- 🔄 Simulation capabilities

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
