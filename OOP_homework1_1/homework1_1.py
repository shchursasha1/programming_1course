class Vector:
    def __init__(self, *components):
        self.components = components

    def dimension(self) -> int:
        return len(self.components)

    def length(self) -> float:
        n = self.dimension()
        return (sum(self.components[i]**2 for i in range(n))) ** 0.5
    
    def arithmetic_avg(self) -> float:
        return sum(self.components) / len(self.components)
    
    def max_component(self):
        return max(self.components)
    
    def min_component(self):
        return min(self.components)
    
    def __copy__(self):
        return Vector(*self.components)
    
    def __repr__(self):
        return f"Vector{self.components}"
    

def validate(func):
    def wrapper(vectors, *args, **kwargs):
        if not vectors:
            raise ValueError("The vectors list is empty")
        return func(vectors, *args, **kwargs)
    return wrapper


def read_vectors_from_file(filename):
    components = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            components.append(data)
    return components


vectors_data = []
input_files = ["input01.txt", "input02.txt", "input03.txt"]
for filename in input_files:
    vectors_data.extend(read_vectors_from_file(filename))

vectors = [Vector(*map(float, vector)) for vector in vectors_data if len(vector) != 0]


@validate
def max_dimension(vectors):
    max_dimension_vector = max(vectors, key=lambda vector: (vector.dimension(), -vector.length()))
    return max_dimension_vector


@validate
def max_length(vectors):
    max_length_vector = max(vectors, key=lambda vector: (vector.length(), -vector.dimension()))
    return max_length_vector


@validate
def average_length(vectors):
    return sum(vector.length() for vector in vectors) / len(vectors)


@validate
def amount_vector_above_average_length(vectors) -> int:
    counter = 0
    avg_length = average_length(vectors)
    for vector in vectors:
        if vector.length() > avg_length:
            counter += 1
    return counter
            

@validate
def max_max_component(vectors):
    return max([vector for vector in vectors if vector.max_component() == max(vector.max_component() for vector in vectors)], key=lambda vector: vector.min_component(), default=None)


@validate
def min_min_component(vectors):
    return max([vector for vector in vectors if vector.min_component() == min(vector.min_component() for vector in vectors)], key=lambda vector: vector.max_component(), default=None)


print(min_min_component(vectors))