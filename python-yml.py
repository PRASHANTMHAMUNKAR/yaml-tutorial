import yaml

with open("git-build.yml", "r") as file:
    data = yaml.safe_load(file)

print(data)

