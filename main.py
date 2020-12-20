#!/usr/bin/env python3
import yaml
from argparse import ArgumentParser, Namespace
from jinja2 import Template


def main(args: Namespace):
    """

    :param args:
    :return:
    """
    with open(args.topology_file, 'r') as fp:
        render(data=yaml.safe_load(fp),
               path_to_j2=args.template if args.template else "ios-classic.j2")


def render(data: dict, path_to_j2: str):
    """

    :param data:
    :param path_to_j2:
    :return:
    """
    with open(path_to_j2) as file_:
        print(Template(file_.read()).render(data))


if __name__ == "__main__":
    parser = ArgumentParser(description='Render templates for node config')
    parser.add_argument('topology_file', type=str, help='YAML defining topology')
    parser.add_argument('--template', type=str, help='Use a custom template. Default: ./ios-classic.j2')
    main(parser.parse_args())
