import click
from notebook_parameterizer.run import run


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('notebook_path', required=True)
@click.argument('parameters_path', required=True)
@click.option('--output_notebook_path', '-o',
              default=None, help='Path to the parameterized output notebook')
@click.option('--expand_env_values', '-e', is_flag=True,
              default=False, help='Should ENV_ prefixed parameter values be '
                                  'expanded to their matching OS environment '
                                  'variable value')
def notebook_parameterizer(
        notebook_path,
        parameters_path,
        output_notebook_path,
        expand_env_values
):
    return run(notebook_path,
               parameters_path,
               output_notebook_path,
               expand_env_values)
