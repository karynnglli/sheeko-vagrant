import os
import json
from os import listdir
from os.path import isfile, join
# --------------- configuration start here --------------------------------------------------------------------------
# Path to checkpoint file or a directory containing checkpoint files. Passing
# a directory will only work if there is also a file named 'checkpoint' which
# lists the available checkpoints in the directory. It will not work if you
# point to a directory with just a copy of a model checkpoint: in that case,
# you will need to pass the checkpoint path explicitly.
# fine tuning model using original data set

'''Path to the directory containing the checkpoint file (pre-trained model)'''
CHECKPOINT_PATH="path/to/dir/pretrained_model"

# Vocabulary Dictionary file generated by the preprocessing script.
VOCAB_FILE = "path/to/dir/pretrained_model/word_count.txt"

# Path to the JPEG image file to generate caption.
IMAGE_FILE = "path/to/file/test_image.jpg"

# -------------------configuration end here-----------------------------------------------------------------------

CODE_PATH = "../../library/"

# Run inference to generate captions.
os.system(
   "python " + CODE_PATH + "run_inference_demo.py --checkpoint_path=" + CHECKPOINT_PATH + " --vocab_file=" + VOCAB_FILE + " --input_files=" + IMAGE_FILE)

print("Caption Generating Demo Completed!")
press = raw_input("Press any key to quit \n")