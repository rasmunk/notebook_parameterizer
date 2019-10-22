import sys
import os
import nbformat
from papermill.parameterize import read_yaml_file
from papermill.translators import papermill_translators

this_path = os.path.dirname(__file__)


def run(notebook_path,
        parameters_path,
        output_notebook_path=None,
        expand_env_values=False
        ):
    if not os.path.exists(notebook_path):
        return -1

    if not os.path.exists(parameters_path):
        return -2

    # Load input notebook
    input_nb = nbformat.read(notebook_path, as_version=4)
    kernel_name = input_nb.metadata.kernelspec.name
    language = input_nb.metadata.kernelspec.language
    translator = papermill_translators.find_translator(kernel_name, language)

    # Load input parameter yaml file as dict
    parameters = read_yaml_file(parameters_path)

    # Find each
    cells = input_nb.get('cells')
    code_cells = [(idx, cell) for idx, cell in enumerate(cells)
                  if cell.get('cell_type') == 'code']
    for idx, cell in code_cells:
        cell_updated = False
        source = cell.get('source')
        # Either single string or a list of strings
        if isinstance(source, str):
            lines = source.split('\n')
        else:
            lines = source

        for idy, line in enumerate(lines):
            if "=" in line:
                d_line = list(map(lambda x: x.replace(' ', ''),
                                  line.split('=')))
                # Matching parameter name
                if len(d_line) == 2 and d_line[0] in parameters:
                    value = parameters[d_line[0]]
                    # Whether to expand value from os env
                    if expand_env_values and isinstance(value, str) and \
                            value.startswith("ENV_"):
                        env_var = value.replace("ENV_", "")
                        value = os.getenv(
                            env_var,
                            "MISSING ENVIRONMENT VARIABLE: {}".format(env_var))
                    lines[idy] = translator.assign(
                        d_line[0], translator.translate(value))

                    cell_updated = True
        if cell_updated:
            cells[idx]['source'] = '\n'.join(lines)

    # Validate that the parameterized notebook is still valid
    try:
        nbformat.validate(input_nb, version=4)
    except nbformat.ValidationError:
        return -3

    try:
        nbformat.write(input_nb, output_notebook_path, version=4)
    except IOError as err:
        print("Failed to write the output notebook %s, error: %s"
              % (output_notebook_path, err))
        return -4


if __name__ == "__main__":
    _, notebook_path, parameters_path, output_notebook_path, expand_env_values\
        = sys.argv
    run(notebook_path, parameters_path, output_notebook_path,
        expand_env_values)
