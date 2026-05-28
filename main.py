from preprocess.validation import run_validation_pipeline
from preprocess.preprocessing import run_preprocessing_pipeline
from analytics.feature import feature_data
from analytics.analytics import run_anaylzed_pipeline
from analytics.intelligence_layer import generate_intelligence_contract
from analytics.analysis_contact_v1 import analysis_contract
from visualization.output import run_output_file


def run_main_pipeline():

    df = run_validation_pipeline()
    df = run_preprocessing_pipeline(df)
    df = feature_data(df)
    df = run_anaylzed_pipeline()
    df = generate_intelligence_contract(df)
    df = analysis_contract(df)
    df = run_output_file()
    return df

run_main_pipeline()