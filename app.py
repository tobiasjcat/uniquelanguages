#/usr/bin/env python3

#Paul Croft
#November 19, 2020

from flask import Flask
app = Flask(__name__)

import json

#Load everything into RAM
language_data = json.load(open("all_compiled.json"))

@app.route("/v1/region/<rname>", methods = ["GET"])
def get_region(rname):
	if rname in language_data:
		return language_data[rname]
	return "Region not recognized", 404


def main():
	app.run(debug=False)
	return 0

if __name__ == '__main__':
	exit(main())