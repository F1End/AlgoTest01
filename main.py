from algo import algo2 as algo


def run_algo(provider_avaibility, clients):
    provider = algo.Provider(provider_avaibility)
    calendar = algo.TimeMatrix(provider, clients)
    calendar.sum_values()
    print(calendar.matrix.to_string())


"""Variables for testing"""
provider_avaibility_time = ["Mon: 8", "Mon: 10", "Mon: 12", "Tue: 8", "Tue: 10", "Tue: 12", "Wed: 10", "Wed: 12"]

client1 = algo.Client("Anna", ["Mon: 8", "Mon: 10", "Mon: 12", "Tue: 8", "Tue: 10"])
client2 = algo.Client("Bea", ["Tue: 10", "Tue: 12", "Wed: 10"])
client3 = algo.Client("Cecil", ["Mon: 12", "Tue: 8", "Tue: 10"])
client4 = algo.Client("Dia", ["Tue: 12"])
client_list = [client1, client2, client3, client4]


if __name__ == "__main__":
    run_algo(provider_avaibility_time, client_list
             )