"""Functional tests with the CLI."""
import os
import subprocess


def save_fixture(cli_output):
    """Tool to save the output of the CLI to a file for next test."""
    with open('fixtures/cli/expected_cli_output_engnr.txt', 'w', encoding='utf-8') as f2:
        f2.write(cli_output.stdout)


def test_cli_interface(download_tmpdir):
    """Test the CLI interface."""
    try:
        with open('fixtures/cli/expected_cli_output_engnr.txt', 'r', encoding='utf-8') as f:
            expected_cli_output = f.read()
            cli_output = subprocess.run(
                ['poetry', 'run', 'page-loader', '-o', download_tmpdir, 'https://engnr.dev'],
                check=True,
                capture_output=True,
                text=True,
                encoding='utf-8',
                shell=False,
            )

            # save_fixture(cli_output)  # Uncomment to fixture preparation. # noqa: E800

            path = os.path.join(download_tmpdir, 'engnr-dev.html')  # get the path to the downloaded file
            expected_cli_output_r = expected_cli_output.format(path=path)   # replace the path in template

            assert cli_output.stdout == expected_cli_output_r

    except subprocess.CalledProcessError as error:  # handle case if the return code was non-zero
        print(error.stdout)
        print(error.stderr)
        raise error
