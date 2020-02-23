import os
import subprocess
import sys

import config
import const


def cls():
    """Clear the console"""
    os.system('clear')


def enter_case():
    """Accept the answer from user"""
    case = input('>> ')

    return case


def check_version():
    """Requests the current version of the script from the server"""
    actual_version = subprocess.check_output(['curl', '-s', const.url_check_version], encoding='utf-8')
    actual_version = float(actual_version)

    return actual_version


def update_script():
    """Updates the script from the repository to the latest version"""
    upd = f'wget -nv -O - {const.url_update} > {config.path_to_script}/last_update.tar.xz'
    tar = f'tar -xvf {config.path_to_script}/last_update.tar.xz -C {config.path_to_script}'
    chmod = f'chmod +x {config.path_to_script}/main_script.py'
    rm = f'rm -f {config.path_to_script}/last_update.tar.xz'

    actual_version = check_version()
    print('\n> Update\n')
    if actual_version > const.version:
        print('There is an update!')
        print(f'Current version: {actual_version}\nInstalled Version: {const.version}\n\nDownload update? [Y/n]\n')
        case = enter_case()
        if case.lower() == 'y':
            print('\nDownload the archive with the latest version of the script:')
            os.system(upd)
            print('\nUnpack:')
            os.system(tar)
            print('\nAssign rights to enforce...\n')
            os.system(chmod)
            os.system(rm)
            print('\nDone! The script will be closed to apply the update.\n')
            input('Press Enter to close the script...')
            cls()
            sys.exit()
        elif case.lower() == 'n':
            input('\nUpdate canceled. Press Enter to return to the main menu...')
        else:
            input('\nIncorrect option entered. Press Enter to return to the main menu...')
    else:
        print('There is no update, try later :(\n')
        input('Press Enter to return to the main menu...')


if __name__ == '__main__':
    update_script()
