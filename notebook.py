from scripts.extract import extract
from scripts.clean import clean
from scripts.load import load

# Run the pipeline
extract()
clean()
load()