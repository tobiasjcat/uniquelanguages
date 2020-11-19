#!/usr/bin/env python3

#Paul Croft
#November 19, 2020


import json
import os
from operator import itemgetter
from pprint import pformat, pprint


def main():
    regions = os.listdir("data")

    results = {}

    for region in regions:
        regions_languages = set()
        region_json = json.load(open("data/{}".format(region)))
        for country in region_json:
            regions_languages.update(map(itemgetter("name"),country["languages"]))        
        results[region.split('.',1)[0]] = json.dumps(sorted(list(regions_languages)))

    with open("all_compiled.json", 'w') as outfile:
        json.dump(results, outfile)


if __name__ == '__main__':
    exit(main())
