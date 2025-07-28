import numpy as np


class RecommendationSystem:
    def __init__(self, k):
        self.data = []
        self.visited = []
        self.k = k

    def get_mean(self, data):
        return np.mean(data, axis=0)

    def without_visited(self):
        visited_set = set([str(x) for x in self.visited])
        data_without_visited = np.array([x for x in self.data if str(x) not in visited_set])
        return data_without_visited

    def get_k_neighbours(self, point):

        data_without_visited = self.without_visited()
        if len(data_without_visited) < self.k:
            raise Exception("Quantity of objects is less than k")

        sorted_data = sorted(data_without_visited, key=lambda x:np.linalg.norm(point - x))
        return sorted_data[:self.k]


    def fit(self, visited, data):
        if not type(data) == np.ndarray:
            raise Exception("data must have numpy.ndarray type")
        self.visited = visited
        self.data = data

    def predict(self, indexes = False):
        mean = self.get_mean(self.visited)

        if indexes:
            dict = {str(obj): i for obj, i in zip(self.data, range(0, len(self.data)))}
            neighbours = self.get_k_neighbours(mean)
            prediction_indexes = np.array([dict[str(neighbour)] for neighbour in neighbours])
            return prediction_indexes

        return self.get_k_neighbours(mean)
