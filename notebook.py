from scripts.extract import extract
from scripts.clean import clean
from scripts.load import load
from scripts.analyze import analyze

# Run the pipeline
extract()
clean()
load()
analyze()
