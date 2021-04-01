from tensorflow_addons.optimizers import Triangular2CyclicalLearningRate

def cyclical_learning_rate_schedule(lr_max, n_items, bs=64, step_size=8):
    maximal_learning_rate=lr_max
    initial_learning_rate=maximal_learning_rate/10
    iterations_in_epoch = n_items//bs
    step_size = iterations_in_epoch * step_size

    cyclical_learning_rate = Triangular2CyclicalLearningRate(initial_learning_rate=initial_learning_rate, 
    maximal_learning_rate=maximal_learning_rate, 
    step_size=step_size)

    return cyclical_learning_rate
