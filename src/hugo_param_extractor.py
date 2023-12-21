#!/usr/bin/env python3.10
import os
import sys
import re
import yaml
import argparse

def extract_hugo_params(html_content):
    """
    Extract Hugo parameters from HTML content and categorize them into Site and Normal parameters.

    Args:
        html_content (str): HTML content of a Hugo theme file.

    Returns:
        dict: A dictionary with keys 'Site' and 'Params', each containing a set of extracted parameters.
    """
    pattern = r'{{\s*([\.\w\s|]+)\s*}}'
    matches = re.findall(pattern, html_content)

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
    Traverse the given directory and extract Hugo parameters from HTML files.

    Args:
        dir_path (str): Path to the Hugo theme directory.

    Returns:
        dict: A dictionary with categorized Hugo parameters.
    """
    categorized_params = {"Site": set(), "Params": set()}
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as html_file:
                    content = html_file.read()
                    params = extract_hugo_params(content)
                    categorized_params["Site"].update(params["Site"])
                    categorized_params["Params"].update(params["Params"])
    return categorized_params

def save_to_yaml(categorized_params, output_file):
    """
    Save the categorized parameters to a YAML file.

    Args:
        categorized_params (dict): Dictionary of categorized Hugo parameters.
        output_file (str): Output file path for the YAML file.
    """
    organized_params = {"Site params": list(categorized_params["Site"]),
                        "Normal params": list(categorized_params["Params"])}
    with open(output_file, 'w') as file:
        yaml.dump(organized_params, file, default_flow_style=False)

def main():
    parser = argparse.ArgumentParser(description="Extract and categorize Hugo parameters from a theme directory.")
    parser.add_argument("theme_dir", help="Path to the Hugo theme directory.")
    parser.add_argument("-o", "--output", default="hugo_theme_params.yaml",
                        help="Output YAML file name. Default is 'hugo_theme_params.yaml'.")
    args = parser.parse_args()

    categorized_params = traverse_theme_directory(args.theme_dir)
    save_to_yaml(categorized_params, args.output)
    print(f"Parameters extracted and categorized. Output saved to {args.output}")

if __name__ == "__main__":
    main()
