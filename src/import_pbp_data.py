import argparse
import datetime
import os
from textwrap import dedent

from src.data_utils import clean_nfl_data, load_pbp_data, process_dataframe, update_dataset


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Get Play-by-Play Data with nfl_data_py",
        epilog=dedent(
            """\
            FURTHER READING
            ---------------

            Subject                             Link
            -------                             ----
            Field Descriptions:                 https://www.nflfastr.com/articles/field_descriptions.html
        """
        ),
    )

    year_metavar = "YYYY"

    # Add arguments for all hyperparameters
    parser.add_argument(
        "-s", "--start-year", type=int, metavar=year_metavar, required=False, default=1999, help="Starting Season.  Default: 1999"
    )
    parser.add_argument(
        "-e",
        "--end-year",
        type=int,
        metavar=year_metavar,
        required=False,
        default=get_current_season_year(),
        help=f"Ending Season.  Default: {get_current_season_year()}",
    )
    parser.add_argument(
        "-d",
        "--dataset",
        type=str,
        metavar="DATASET_NAME",
        required=False,
        default="NFL Play-by-Play Data",
        help="Dataset Name.  Default: NFL Play-by-Play Data",
    )
    parser.add_argument(
        "-p", "--project", type=str, metavar="PROJECT_NAME", required=False, default="NFL Models", help="Project Name.  Default: NFL Models"
    )

    args = parser.parse_args()
    import_pbp_data(args)


def import_pbp_data(args):
    years = list(range(args.start_year, args.end_year + 1, 1))
    file_prefix = "pbp_data"
    os.makedirs(file_prefix, exist_ok=True)
    print(f"Importing Play-by-Play Data for the following years:\n{years}")
    pbp_df = load_pbp_data(years)
    print(f"Cleaning Play-by-Play Data")
    pbp_data = clean_nfl_data(pbp_df)
    print(f"Saving Play-by-Play Data to CSV")
    process_dataframe(pbp_data, file_prefix)
    update_dataset(dataset_name=args.dataset, dataset_project=args.project, file_prefix=file_prefix)


def get_current_season_year():
    # return datetime.datetime.now().year
    return 2023
