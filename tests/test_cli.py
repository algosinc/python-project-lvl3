import subprocess


def test_command_works_properly():
    # try:
        result = subprocess.run(['poetry', 'run', 'page-loader', '-o', 'tmp3', 'https://engnr.dev'],
                                check=True, capture_output=True, text=True, encoding='utf-8')
    # except subprocess.CalledProcessError as error:
        print(result.stdout)
        print(result.stderr)
        # raise error