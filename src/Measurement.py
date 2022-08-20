# this is the key datastructure for a single measurement object
# one measurement always contains:
# * material specifications dataframe (just first row is important here)
# * a fds results dataframe
#
from dataclasses import dataclass
import pandas as pd


@dataclass(order=True, frozen=True)
class Measurement:
    material: pd.DataFrame
    fds_results: pd.DataFrame

    def __init__(self, measurements_df, fds_results_df):
        # drop first two unnecessary rows
        measurements_df = measurements_df.drop([0, 1], axis=0)
        object.__setattr__(self, 'material', measurements_df)
        object.__setattr__(self, 'fds_results', fds_results_df)

    def get_name(self):
        if self.material.empty:
            return

        # name is at first row second column in material dataframe
        return self.material.iat[0, 1]

    def get_serial_number(self):
        if self.material.empty:
            return

        # name is at first row sixth column in material dataframe
        return self.material.iat[0, 5]

    def get_best_result(self):
        # TODO: find best result from dataframe fds_results
        return

    # TODO: add more methods that (transform) and return data we want to display
