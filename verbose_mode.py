import argparse

def verbose_mode():
    parser = argparse.ArgumentParser(description='Run script')
    parser.add_argument('--verbose', help='verbose mode', action='store_true')
    args=parser.parse_args()
    return args.verbose

if __name__=='__main__':
    if verbose_mode():
        print('on')
    else:
        print('off')
