from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('rf.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the form (example with 16 inputs matching your independent variables)
        data = [float(request.form.get(key)) for key in [
            'lever_position', 'ship_speed', 'gt_shaft_torque', 'gt_rate_revolutions',
            'gg_rate_revolutions', 'starboard_propeller_torque', 'port_propeller_torque',
            'turbine_exit_temp', 'compressor_inlet_temp', 'compressor_outlet_temp',
            'turbine_exit_pressure', 'compressor_inlet_pressure', 'compressor_outlet_pressure',
            'exhaust_gas_pressure', 'turbine_injection_control', 'fuel_flow'
        ]]

        # Predict using the model
        prediction = model.predict([data])
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
