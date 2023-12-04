import json 
import pandas as pd


def load_jsonl(filepath):
    data = []
    with open(filepath, 'r') as jsonl_file:
        for line in jsonl_file:
            data.append(json.loads(line.strip()))

    return data


def save_jsonl(data, filepath):
    with open(filepath, "w") as jsonl_file:
        for item in data:
            jsonl_file.write(json.dumps(item) + '\n')

    print("Data saved to ", filepath)


def count_aspect_polarity(list_of_dicts):
    counts = {}
    for converted_dict in list_of_dicts:
        for i in converted_dict['aspects']:
            aspect = i['aspect']
            polarity = i['polarity']
            
            if aspect not in counts:
                counts[aspect] = {}
            
            if polarity in counts[aspect]:
                counts[aspect][polarity] += 1

            else:
                counts[aspect][polarity] = 1
            
    df = pd.DataFrame.from_dict(counts)
    stacked_df = pd.DataFrame(df.stack(), columns=["counts"]).reset_index(names=["polarity", "aspect"])
    
    return df, stacked_df