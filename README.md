# Data Visualization Package

A Python package for data visualization, including interactive and custom graphs.

## Features

- Creation of line, bar and scatter graphs.
- Interactive view with zoom and pan support.
- Export of graphics to PNG, SVG, and PDF formats.

## Installation

You can install the package directly from GitHub or PyPI:

```bash
pip install git+https://github.com/gvicencotti/image_processing_package.git
```

## Data Visualization Package

from image_processing_package.data_loader import load_csv
from image_processing_package.plotter import plot_line

df = load_csv('dados.csv')
plot_line(df, 'x', 'y')

## Credits

This project was developed with the help of OpenAI's ChatGPT, which contributed to defining the scope and provided implementation suggestions. Using AI tools like ChatGPT helped streamline the development process and refine the package's functionality.

## License

[MIT](https://choosealicense.com/licenses/mit/)
