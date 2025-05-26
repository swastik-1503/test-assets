from azure.ai.ml import MLClient, UserIdentityConfiguration
from azure.identity import (
    DefaultAzureCredential,
    InteractiveBrowserCredential,
)
import yaml
def main():
    try:
        credential = DefaultAzureCredential()
        # Check if given credential can get token successfully.
        credential.get_token("https://management.azure.com/.default")
    except Exception:
        # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
        credential = InteractiveBrowserCredential()
    ml_client_registry = MLClient(credential, registry_name="azureml-preview-test1")
    data = parse_yaml()
    print(data['properties'])
    print("\n")
    print(data['tags'])
    readme_content = parse_readme()
    print(readme_content)
    models = ml_client_registry.models.list(name="sklearn_custom")
    for model in models:
        if int(model.version) == 2:
            model.tags = data['tags']
            model.properties = data['properties']
            model.description = readme_content
            ml_client_registry.models.create_or_update(model)
            print(model.name)


def parse_yaml():
    file_path = "spec.yaml"
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data
def parse_readme():
    with open('description.md', 'r', encoding='utf-8') as file:
        readme_content = file.read()
    return readme_content
if __name__ == "__main__":
    main()