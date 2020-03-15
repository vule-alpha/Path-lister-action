import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    # yaml_path = os.environ["INPUT_PATH"]
    # strict = os.environ["INPUT_STRICT"] == "true"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # f=open("output.txt", "w")

    path_count = 0
    for root, dirs, files in os.walk(dir_path):
    	for file in files:
    		if file.endswith('.yml'):
                path_count = path_count + 1
                print(root+'\\'+str(file)+'\n')
                # f.write(root+'\\'+str(file)+"\n")

    print(f"::set-output name=paths::{path_count}")
    set_action_output('paths', path_count)

    # f.close()

    sys.exit(0)


if __name__ == "__main__":
    main()
