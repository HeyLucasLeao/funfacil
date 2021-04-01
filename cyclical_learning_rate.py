from tensorflow_addons.optimizers import CyclicalLearningRate

def cyclical_learning_rate_schedule(lr_max, n_items, bs=64):
  maximal_learning_rate=lr_max
  initial_learning_rate=maximal_learning_rate/10
  epochs_within_each_step = 2
  iterations_in_epoch = n_items//bs
  step_size = iterations_in_epoch * epochs_within_each_step
  cycles = step_size * 2
  training_steps= cycles * 3

  cyclical_learning_rate = CyclicalLearningRate(initial_learning_rate=initial_learning_rate, 
  maximal_learning_rate=maximal_learning_rate, 
  step_size=step_size, 
  scale_fn=lambda x: 1 / (2.0 ** (x - 1))) #triangular2

  return cyclical_learning_rate
