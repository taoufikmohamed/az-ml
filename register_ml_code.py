import argparse
from azureml.core import Workspace, ScriptRunConfig, Experiment

def register_ml_code(ws):
    # Example for registering a script
    experiment = Experiment(workspace=ws, name='my_experiment')
    config = ScriptRunConfig(source_directory='path/to/code', script='train.py')
    run = experiment.submit(config)
    run.wait_for_completion(show_output=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace_name", type=str, required=True)
    parser.add_argument("--resource_group", type=str, required=True)
    parser.add_argument("--subscription_id", type=str, required=True)
    args = parser.parse_args()

    ws = Workspace.get(name=args.workspace_name, resource_group=args.resource_group, subscription_id=args.subscription_id)
    register_ml_code(ws)