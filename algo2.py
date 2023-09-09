import pandas as pd
from typing import List


class Client:
    def __init__(self, name, avaibility):
        self.avaibility = avaibility
        self.name = name


class Provider:
    def __init__(self, preffered_avaibility):
        self.avaibility = preffered_avaibility


class TimeMatrix:
    def __init__(self, provider, clients: List):
        self.provider = provider
        self.clients = clients
        self.matrix = self.construct_matrix()

    def construct_matrix(self):
        df = pd.DataFrame.columns = self.provider.avaibility
        print(self.clients)
        df.insert(0, "client")
        df.insert(1, "client_name")
        return df

    def construct_row(self, client):
        self.matrix.add


provider_avaibility = ["Mon: 8", "Mon: 10", "Mon: 12", "Tue: 8", "Tue: 10", "Tue: 12", "Wed: 10", "Wed: 12"]
provider = Provider(provider_avaibility)

client1 = Client("Anna", ["Mon: 8", "Mon: 10", "Mon: 12", "Tue: 8", "Tue: 10"])
client2 = Client("Bea", ["Tue: 10", "Tue: 12", "Wed: 10"])
client3 = Client("Cecil", ["Mon: 12", "Tue: 8", "Tue: 10"])
client4 = Client("Dia", ["Tue: 12"])

clients = [client1, client2, client3, client4]

calendar = TimeMatrix(provider, clients)
print(calendar.matrix)
