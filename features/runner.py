import os
from behave.__main__ import run_behave
from behave.configuration import Configuration
def main():
    a = os.path.join(os.getcwd(), 'outlookfeatures.feature')
    arguments =(a, )
    configuration = Configuration(arguments)
    for i in range(1):
        run_behave(configuration)


if __name__ == "__main__":
    main()


