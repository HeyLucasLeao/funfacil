from numba import cuda
import tensorflow as tf

physical_device = tf.config.experimental.list_physical_devices('GPU')
try:
  tf.config.experimental.set_memory_growth(physical_device[0], True)
  assert tf.config.experimental.get_memory_growth(physical_device[0])
except:
  print('Invalid device or cannot modify virtual devices once initialized.')
  pass
  
# helps after out of memory errors
device = cuda.get_current_device()
device.reset()
