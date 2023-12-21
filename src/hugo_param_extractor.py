#!/usr/bin/env python3.10
import os
import re
import yaml
import argparse
import json
import xml.etree.ElementTree as ET

def extract_hugo_params(content, file_type):
    """
    Extract Hugo parameters from content based on file type (HTML, JSON, XML)
    and categorize them into Site and Normal parameters.

    Args:
        content (str): Content of a Hugo theme file.
        file_type (str): Type of file ('html', 'json', 'xml').

    Returns:
        dict: A dictionary with keys 'Site' and 'Params', each containing a set of extracted parameters.
    """
    if file_type == 'html':
        pattern = r'{{\s*([\.\w\s|]+)\s*}}'
    elif file_type == 'json':
        pattern = r'"([a-zA-Z0-9_]+)":'
    elif file_type == 'xml':
        pattern = r'<([a-zA-Z0-9_]+)'

    matches = re.findall(pattern, content)

    site_params_set = set()
    normal_params_set = set()
    for match in matches:
        parts = re.findall(r'\.([a-zA-Z0-9_]+)', match)
        for i, part in enumerate(parts):
            if i > 0 and parts[i - 1] == "Site" and part != "Params":
                site_params_set.add(part)
            elif i > 0 and parts[i - 1] == "Params":
                normal_params_set.add(part)

    return {"Site": site_params_set, "Params": normal_params_set}

def traverse_theme_directory(dir_path):
    """
    Traverse the given directory and extract Hugo parameters from HTML, JSON, and XML files.

    Args:
        dir_path (str): Path to the Hugo theme directory.

    Returns:
        dict: A dictionary with categorized Hugo parameters.
    """
    categorized_params = {"Site": set(), "Params": set()}
    layout_params = {}

    for root, dirs, files in os.walk(dir_path):
        layout = os.path.basename(root)
        for file in files:
            file_type = None
            if file.endswith(".html"):
                file_type = 'html'
            elif file.endswith(".json"):
                file_type = 'json'
            elif file.endswith(".xml"):
                file_type = 'xml'

            if file_type:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    params = extract_hugo_params(content, file_type)
                    categorized_params["Site"].update(params["Site"])
                    categorized_params["Params"].update(params["Params"])

                    if layout not in layout_params:
                        layout_params[layout] = {"Site": set(), "Params": set()}
                    layout_params[layout]["Site"].update(params["Site"])
                    layout_params[layout]["Params"].update(params["Params"])

    return categorized_params, layout_params

def save_to_yaml(categorized_params, layout_params, output_file):
    """
    Save the categorized parameters to a YAML file.

    Args:
        categorized_params (dict): Dictionary of categorized Hugo parameters.
        layout_params (dict): Dictionary of parameters categorized by layout.
        output_file (str): Output file path for the YAML file.
    """
    organized_params = {
        "Site params": list(categorized_params["Site"]),
        "Normal params": list(categorized_params["Params"]),
        "Layout params": {k: {"Site": list(v["Site"]), "Params": list(v["Params"])} for k, v in layout_params.items()}
    }
    with open(output_file, 'w') as file:
        yaml.dump(organized_params, file, default_flow_style=False)

def main():
    parser = argparse.ArgumentParser(description="Extract and categorize Hugo parameters from a theme directory.")
    parser.add_argument("theme_dir", help="Path to the Hugo theme directory.")
    parser.add_argument("-o", "--output", default="hugo_theme_params.yaml",
                        help="Output YAML file name. Default is 'hugo_theme_params.yaml'.")
    args = parser.parse_args()

    categorized_params, layout_params = traverse_theme_directory(args.theme_dir)
    save_to_yaml(categorized_params, layout_params, args.output)
    print(f"Parameters extracted and categorized. Output saved to {args.output}")

if __name__ == "__main__":
    main()
