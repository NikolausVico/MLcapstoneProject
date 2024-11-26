from logic import DQN, ReplayBuffer, VRPAgent, train_vrp_agent
from logic import valid_nodes, valid_demands, distance_matrix, num_actions
import logic
import tensorflow as tf
from keras.models import load_model
# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="vrp_dqn_model.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prepare a dummy input
dummy_input = tf.random.uniform(input_details[0]['shape'], dtype=tf.float32)

# Run inference
interpreter.set_tensor(input_details[0]['index'], dummy_input)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])

print("Inference result:", output_data)

interpreter = (VRPAgent(num_actions=num_actions))
routes_new = train_vrp_agent(interpreter, num_vehicles=1, capacity=100, customer_demands=valid_demands, distance_matrix=distance_matrix)