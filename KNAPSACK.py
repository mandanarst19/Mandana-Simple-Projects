from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel


weights = [2, 5, 7] 
values = [1, 6, 8]   
weight_limit = 10    
bqm = BinaryQuadraticModel('BINARY')
for i, value in enumerate(values):
    bqm.add_variable(i, -value)
lagrange_multiplier = max(values)
for i, weight in enumerate(weights):
    bqm.add_variable(i, lagrange_multiplier * (weight - weight_limit)**2)
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=100)
best_solution = sampleset.first.sample
selected_items = [index for index, presence in best_solution.items() if presence == 1]
print(f'Selected items: {selected_items}')
