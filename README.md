# HugoParamExtractor
Author: Amir Ahmed - `amirtheahmed@gmail.com` - [website](amirtheahmed.dev)

HugoParamExtractor is a Python script designed for Hugo developers. It scans Hugo theme files, including HTML, JSON, and XML formats, and extracts the parameters used in the templates. This aids theme creators and developers in easily discovering and documenting their theme's configurable options.

## Features
- Supports parsing HTML, JSON, and XML files within Hugo themes.
- Extracts and categorizes parameters into 'Site' and 'Normal' parameters.
- Organizes parameters by layout/folder names, enhancing clarity for theme developers.

## Installation

To use HugoParamExtractor, ensure you have Python 3 installed on your system.

1. Clone this repository or download the source code.
2. Navigate to the `HugoParamExtractor` directory.
3. No external dependencies are required as the script uses standard Python libraries.

## Usage
Run the script by passing the path to your Hugo theme directory as an argument:

```bash
python src/hugo_param_extractor.py /path/to/your/hugo/theme
```
The script will create a hugo_theme_params.yaml file in the current directory, listing all the parameters used in your theme, organized by category and layout.

## License
This project is licensed under the MIT License.