# HugoParamExtractor
author: Amir Ahmed - `amirtheahmed@gmail.com` - [website](amirtheahmed.dev)

HugoParamExtractor is a Python script for Hugo developers. It scans Hugo theme files and extracts the parameters used in the templates, helping theme creators and developers to easily discover/document their theme's configurable options.

## Installation

To use HugoParamExtractor, you need Python 3 installed on your system.

1. Clone this repository or download the source code.
2. Navigate to the `HugoParamExtractor` directory.
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

## Usage
Run the script by passing the path to your Hugo theme directory as an argument:

    ```bash
    python src/hugo_param_extractor.py /path/to/your/hugo/theme

The script will create a hugo_theme_params.yaml file in the current directory, listing all the parameters used in your theme.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## License
This project is MIT licensed.


### requirements.txt
The `requirements.txt` will list the dependencies required by the script. Since we're using standard libraries only, this file may not be necessary. However, if you decide to use any external libraries in the future, you would list them here.

### Final Steps
- Test the script thoroughly to ensure it works as expected.
- Push the code to a public repository on GitHub or similar platforms.
- Share the repository link in communities, forums, or social media platforms where Hugo theme developers are active.

This structure and documentation will help make your tool accessible and user-friendly for the community.

