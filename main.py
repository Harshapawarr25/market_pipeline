from clean_data import run_clean_pipeline
from preprocessing import run_preprocessing_pipeline
from output import run_output_file

def run_main_pipeline():

    df = run_clean_pipeline()
    df = run_preprocessing_pipeline(df)
    df = run_output_file()
    return df
run_main_pipeline()