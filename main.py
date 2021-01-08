#!/usr/bin/env python3
"""Script for rendering config for topologies defined by a YAML file"""
from argparse import ArgumentParser, Namespace
import yaml
from jinja2 import Template


def main(args: Namespace):
    """First method called when ran as a script"""
    with open(args.topology_file, "r") as fp_:
        render(
            data=yaml.safe_load(fp_),
            path_to_j2=args.template if args.template else "ios-classic.j2",
        )


def render(data: dict, path_to_j2: str):
    """Renders given Jinja2 template with given data (dict)

    Args:
        data: Dict object containing structured data valid for given Jinja template
        path_to_j2: Filepath to Jinja template
    """
    with open(path_to_j2) as file_:
        print(Template(file_.read()).render(data))


if __name__ == "__main__":
    parser = ArgumentParser(description="Render templates for node config")
    parser.add_argument("topology_file", type=str, help="YAML defining topology")
    parser.add_argument(
        "--template", type=str, help="Use a custom template. Default: ./ios-classic.j2"
    )
    main(parser.parse_args())
