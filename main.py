from preprocess.preprocessing import run_preprocessing_pipeline
from preprocess.validation import run_validation_pipeline
from analytics.analytics import run_clean_pipeline
from analytics.feature import feature_data
from visualization.output import run_output_file

def run_main_pipeline():

    df = run_clean_pipeline()
    df = run_preprocessing_pipeline(df)
    df = run_validation_pipeline()
    df = feature_data(df)
    df = run_output_file()
    return df

run_main_pipeline()