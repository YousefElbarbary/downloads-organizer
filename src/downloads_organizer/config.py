import yaml
from pathlib import Path
def load_yaml():
    with open(Path(__file__).parent.parent.parent / "config" / "categories.yaml", 'r') as file:
            return(yaml.safe_load(file))

def flatten_dict(d, items_dict, parent_key = '', ignore_keys = {'categories', "fallback", "extensions"}):
        for key, value in d.items():
            if key in ignore_keys:
                new_key = Path(parent_key)
            else:
                new_key = Path(parent_key) / key if parent_key else Path(key)

            if isinstance(value, dict):
                flatten_dict(value, items_dict, new_key)
            else:
                if value:
                    for each_value in value: 
                        items_dict[each_value] = new_key
                else:
                    items_dict[value] = new_key
        return(items_dict)

def load_config():
     items_dict = dict()
     config = load_yaml()
     print(flatten_dict(config, items_dict))