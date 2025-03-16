import argparse
from azureml.core import Workspace, Dataset

def register_datasets(ws):
    # Example for registering a dataset from a datastore
    datastore = ws.get_default_datastore()
    dataset = Dataset.File.from_files(path=(datastore, 'path/to/data'))
    dataset.register(workspace=ws, name='my_dataset', description='My dataset description')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace_name", type=str, required=True)
    parser.add_argument("--resource_group", type=str, required=True)
    parser.add_argument("--subscription_id", type=str, required=True)
    args = parser.parse_args()

    ws = Workspace.get(name=args.workspace_name, resource_group=args.resource_group, subscription_id=args.subscription_id)
    register_datasets(ws)