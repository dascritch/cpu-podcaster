#!/usr/bin/python3

segments = []

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