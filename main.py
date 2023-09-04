import yaml
import json

# Define the input and output file names
input_yaml_file = "openAi.yaml"
output_json_file = "openai.json"

# Open and read the YAML file
with open(input_yaml_file, 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Write the data as JSON to the output file
with open(output_json_file, 'w') as json_file:
    json.dump(yaml_data, json_file, indent=4)

print(f"Conversion from YAML to JSON completed. Data saved in {output_json_file}")
