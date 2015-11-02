#!/usr/bin/python3

import json, os


temporary_wav_file = 'cut.wav'

segments = []
parameters = {
	'public_html_path'  : 'CPU/onweb',
	'program_name'      : 'CPU',
	'copyright'			: 'DaScritch & partners pour Radio FMR',
	'website'			: 'http://cpu.dascritch.net'
}

with open('./parameters.json', 'r') as parfile:
	parameters.update(json.load(parfile))

print(parameters)

# get from file
program_number = '0007'
date_hyphen = '29-10-15'
subject = 'Noms de domaines'
trigger = 'Noms de domaines' # or segment name

# date recalculation
dp = date_hyphen.split('-')
date_year = '20{}'.format(dp[2])
date_slashed = '{}/{}/{}'.format(dp[0], dp[1], date_year)

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

def encode(source_file):
	if os.path.isfile(temporary_wav_file):
		os.remove(temporary_wav_file)
	exe_line = 'oggenc -t "{program_name}: {subject} ({date_slashed})" -d "{date_slashed}" -N "{program_number}" -a "{copyright}" -G "radio" -l "{website}" -c "{subject}" -q 6 -o "{path}/{program_number}-${trigger}-({date_hyphen}).ogg" {wav}'.format(
		program_name=parameters['program_name'],
		copyright=parameters['copyright'],
		website=parameters['website'],
		path=parameters['public_html_path'],
		wav=temporary_wav_file,
		program_number=program_number,
		date_hyphen=date_hyphen,
		date_slashed=date_slashed,
		date_year=date_year,
		subject=subject,
		trigger=trigger
		) 
	print ("\n",exe_line)
	exe_line = 'lame -h -b 128 -B 224 --tt "{program_name} ({date_slashed})" --tn {program_number} --ta "{copyright}" --tl "{website}" --ty {date_year} --tg 20 --tc "{subject}" {wav} "{path}/podcast/{program_number}-{trigger}-({date_hyphen}).mp3"'.format(
		program_name=parameters['program_name'],
		copyright=parameters['copyright'],
		website=parameters['website'],
		path=parameters['public_html_path'],
		wav=temporary_wav_file,
		program_number=program_number,
		date_hyphen=date_hyphen,
		date_slashed=date_slashed,
		date_year=date_year,
		subject=subject,
		trigger=trigger
		)
	print ("\n",exe_line)

	temporary_wav_file


# main section

decode_track_txt()
print(segments)
encode('pad.wav')
