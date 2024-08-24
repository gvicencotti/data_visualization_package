# Data Visualization Package

A Python package for data visualization, including interactive and custom graphs.

## Features

- Creation of line, bar, and scatter graphs.
- Interactive view with zoom and pan support.
- Export of graphics to PNG, SVG, and PDF formats.

## Installation

You can install the package directly from PyPI:

```bash
pip install data-visualization-package==0.1.5
```

## Usage Instructions

Basic example on how to use the package:
from data_visualization_package.data_loader import load_csv
from data_visualization_package.plotter import plot_line

df = load_csv('path/to/your_data.csv')

plot_line(df, 'x_column', 'y_column')

**Parameters**
- file_path: The path to the CSV file you want to load.
- dataframe: The DataFrame containing your data.
- x_column: The name of the column to be used for the x-axis.

**Supported Graphs**
- Line Graphs
- Bar Graphs
- Scatter Graphs

## Running Tests

Install pytest:
```bash
pip install pytest
```
Run the Tests:
```bash
python -m pytest tests/
```

## Credits
This project was developed with the help of OpenAI's ChatGPT, which contributed to defining the scope and provided implementation suggestions. Using AI tools like ChatGPT helped streamline the development process and refine the package's functionality.

## License
[MIT](https://choosealicense.com/licenses/mit/)
