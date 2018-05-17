import argparse
from gtd.io import save_stdout
from gtd.log import set_log_level
from gtd.utils import Config
from textmorph.edit_model.training_run import EditTrainingRuns

from textmorph.edit_model.editor import EditExample
set_log_level('DEBUG')

from textmorph import data

# create experiment
experiments = EditTrainingRuns(check_commit=False)

# dictionary of composers and checkpoints
# composer={'bach':63, 'beethoven':62, 'brahms':28, 'handel':64, 'haydn':x, 'mozart':65, 'schubert':x, 'vivaldi':x}
TYPE='mono'
composer={'bach':63, 'brahms':28}

for key in composer:
	print('Processing ', key, '...')
	EDIT_RUN=composer[key]
	# create an experiment from saved checkpoint
	exp = experiments.get(EDIT_RUN)
	editor = exp.editor

	test=['holdout', 'split']
	for t in test:
		path = c+'_'+TYPE+'_'+test+'.txt'
		with open(path) as file:
			line=f.readlines():
			ex = EditExample.salient_diff(line, line, '')
			print(ex)


			output_words_batch, edit_traces = editor.edit([ex], beam_size=8)
			print('print(edit_traces)')
			print(edit_traces)

			print('print(edit_traces[0])')
			print(edit_traces[0])

			break
		break
	break
