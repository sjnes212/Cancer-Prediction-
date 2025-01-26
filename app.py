from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('data/Cancer.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the ID input from the user
            input_id = request.form.get('id').strip()
            
            # Check if the ID exists in the dataset
            if input_id in data['id'].astype(str).values:  # Convert ID to string for comparison
                # Find the corresponding diagnosis
                diagnosis = data.loc[data['id'].astype(str) == input_id, 'diagnosis'].values[0]
                
                # Determine if cancerous or non-cancerous
                if diagnosis == 'M':
                    result = f"ID {input_id}: Cancer detected (Malignant)"
                elif diagnosis == 'B':
                    result = f"ID {input_id}: No Cancer (Benign)"
                else:
                    result = f"ID {input_id}: Diagnosis unknown"
            else:
                result = f"ID {input_id} not found in the dataset."
        
        except Exception as e:
            result = f"An error occurred: {str(e)}"
        
        return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
