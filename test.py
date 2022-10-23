import argparse
from time import sleep

import pexpect


def main(command):
    """
    - Run ipython using subprocess pipe
    - Wait for input
    - Input command
    - Wait for next input
    - Print result
    :param command:
    :return:
    """
    # Create ipython process
    c = pexpect.spawn('ipython --colors=NoColor')
    c.expect_exact('In [1]:')
    # Send command to process
    c.sendline(command)
    c.expect_exact('In [2]:')
    print(c.before.decode('utf-8'))


if __name__ == '__main__':
    # Parse question from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, help='Command to run in ipython')
    args = parser.parse_args()
    main(args.command)
