class CountVectorizer:
    def __init__(self):
        self.set = set()

    def fit_transform(self, array):
        out_array = []

        for i in range(len(array)):
            arr_i = array[i].split()

            for j in range(len(arr_i)):
                self.set.add(arr_i[j])

        for i in range(len(array)):
            arr_i = array[i].split()
            out_array_j = []

            for item in self.set:
                out_array_j.append(arr_i.count(item))

            out_array.append(out_array_j)

        return out_array

    def get_feature_names(self):
        print(list(self.set))


if __name__ == '__main__':
    c_v = CountVectorizer()
    count_matrix = c_v.fit_transform(['cat dog cow', 'dog rat mouse'])
    c_v.get_feature_names()

    print(count_matrix)
