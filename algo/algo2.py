from typing import List

import pandas as pd
import numpy as np


class Client:
    def __init__(self, name, avaibility):
        self.avaibility = avaibility
        self.name = name

    def __repr__(self):
        return self.name


class Provider:
    def __init__(self, prefered_avaibility):
        self.avaibility = prefered_avaibility


class TimeMatrix:
    def __init__(self, provider, clients: List):
        self.provider = provider
        self.clients = clients
        self.matrix = self.construct_matrix()

    def construct_matrix(self):
        columns = ["client"]
        columns.extend(self.provider.avaibility)
        rows = [self.initiate_rows(clnt) for clnt in self.clients]
        df = pd.DataFrame(rows, columns=columns)
        return df

    def initiate_rows(self, client):
        row_data = [client]
        for timeslot in self.provider.avaibility:
            if timeslot in client.avaibility:
                row_data.append(1)
            else:
                row_data.append(0)
        return row_data

    def sum_values(self):
        self.matrix['option_count'] = self.matrix[list(self.matrix.columns)].sum(axis=1, numeric_only=True)

    def construct_row(self, client):
        """
        For clients added later, not in initial construction.
        :param client:
        :return:
        """
        row = {col: 0 for col in self.matrix.columns}
        row["client"] = client
        for col in self.matrix.columns:
            if col in client.avaibility:
                pass

    def update_row(self, client):
        """
        For data update on already added clients
        :param client:
        :return:
        """
