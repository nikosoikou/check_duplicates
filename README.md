# check_duplicates

This package provides a function for checking duplicates in a pandas DataFrame.

## Installation

To install the package, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the `check_duplicates` function, import it from the package and pass a pandas DataFrame and a list of columns to check for duplicates. The function returns a dictionary with two items:

- `count`: the number of cases where duplicates occur.
- `samples`: a DataFrame with group count of duplicate rows for the columns from the input,
  e.g.: col_1, col_2, number_of_duplicates

## Example

```python
import pandas as pd
from src.main import check_duplicates

# Create a sample DataFrame
df = pd.DataFrame(
    data=[
        ['A', 'a', 'x', 1],
        ['A', 'b', 'x', 1],
        ['A', 'c', 'x', 1],
        ['B', 'a', 'x', 1],
        ['B', 'b', 'x', 1],
        ['B', 'c', 'x', 1],
        ['A', 'a', 'y', 1],
    ],
    columns=['col_1', 'col_2', 'col_3', 'col_4']
)

# Check for duplicates
result = check_duplicates(df, ['col_1'])

# Print results
print(result)
```

Here's an example of what the output might look like:

```bash
{ ‘count’: 7, ‘samples’: pd.DataFrame({ ‘col_1’: [‘A’, ‘B’], ‘number_of_duplicates’: [4, 3] }) }
```

In this example, the `count` item indicates that there are 7 cases where duplicates occur, and the `samples` item provides a DataFrame with a group count of duplicate rows for the `col_1` column.


## Testing

To run the tests with pytest, navigate to the root directory of your project in a terminal or command prompt and run the following command:

```bash
pytest
```

This command will run all the tests in the project.

## License
This package is licensed under the MIT License. See the LICENSE file for details.
