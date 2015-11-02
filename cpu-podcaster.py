#!/usr/bin/python3

import json

segments = []
parameters = None

with open('./parameters.json', 'r') as parfile:
	parameters = json.load(parfile)

print(parameters)


def from_col_timecode(text):
	return float(text.replace(',','.'))

def decode_track_txt(filename="markers.txt"):
	with open(filename, 'r') as track_file:
		for line in track_file:
			cols = line.split('\t')
			segments.append({
				'start' : from_col_timecode(cols[0]),
				'end'   : from_col_timecode(cols[1]),
				'type'  : cols[2].split(' : ')[0].strip(),
				'title' : cols[2].split(' : ')[1].strip()
				})
	track_file.close()
	pass



# main section

decode_track_txt()

print(segments)