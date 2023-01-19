#! /usr/bin/env python
"""
Script to generate a sales brochure-like description for a hypothetical
cybersecurity tool using the typical buzzwords.

AUTHOR: raubvogel@gmail.com

RELEASE: 0.1.0.

"""
from random import *
import json


def read_data(file_name: str):
    with open(file_name) as infile:
        return json.load(infile)


def describe_me(the_data: dict):
    """ 
    Build a sentence describing this tool

    """
    print("Our",
       choice(the_data['pattern1']),
      "tool implements a",
       choice(the_data['pattern2']),
       choice(the_data['pattern4']),
      "enabling you to",
       choice(the_data['pattern5']),
      "the",
       choice(the_data['pattern7']),
      "of your",
       choice(the_data['pattern3']),
      "by using our",
       choice(the_data['pattern6']),
      "interface."
     )


if __name__ == "__main__":
    my_data = read_data('data.json')
    describe_me(my_data)
