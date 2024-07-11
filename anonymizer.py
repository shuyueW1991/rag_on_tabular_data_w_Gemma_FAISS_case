import json
import random
import string

def anonymize_json(filename):
  """
  This function anonymizes a JSON file by disrupting numerical values and replacing strings with random letters.

  Args:
      filename: The path to the JSON file.
  """
  with open(filename, 'r') as f:
    data = json.load(f)

  def anonymize_value(value):
    if isinstance(value, (int, float)):
      # Disrupt numerical values by adding/subtracting a random number within a range
      range_limit = 100  # Adjust this range as needed
      disruption = random.uniform(-range_limit, range_limit)
      return value + disruption
    elif isinstance(value, str):
      # Replace string with random letters of same length
      random_letters = ''.join(random.choices(string.ascii_letters, k=len(value)))
      return random_letters
    else:
      # Recursively anonymize nested objects/lists
      return anonymize_object(value) if isinstance(value, dict) else anonymize_list(value)

  def anonymize_list(data_list):
    return [anonymize_value(item) for item in data_list]

  def anonymize_object(data_dict):
    return {key: anonymize_value(value) for key, value in data_dict.items()}

  anonymized_data = anonymize_value(data)

  with open(filename + '.anonymized', 'w') as f:
    json.dump(anonymized_data, f, indent=2)

# Example usage
filename = 'result.json'
anonymize_json(filename)
print(f'JSON anonymized and saved to: {filename}.anonymized')
