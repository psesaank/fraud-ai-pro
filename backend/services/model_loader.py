
import os
import onnxruntime as ort

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model.onnx")
MODEL_PATH = os.path.abspath(MODEL_PATH)

session = ort.InferenceSession(MODEL_PATH)
model = session
input_name = session.get_inputs()[0].name
