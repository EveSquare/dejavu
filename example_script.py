import json

from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

    djv = Dejavu(config)

    djv.fingerprint_directory("test2", [".wav"])
    
    # results = djv.recognize(FileRecognizer, "mp3/2D Drive.mp3")
    # print(f"From file we recognized: {results}\n")