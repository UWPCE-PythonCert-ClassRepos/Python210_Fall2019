#!/usr/bin/env python3


class CLI():
    """
    Class to present a CLI to the user.
    """
    def __init__(self, cli_functions=[]):
        """
        Initialize the CLI class.
        :param cli_functions: Optionally pass in a list of functions at instantiation.
        """
        cli_functions.append(self.quit)  # Add quit() to our probably empty list of functions
        self.cli_functions = cli_functions
        self.cli_message = ("Menu Options\n")
        self.cli_options_template = "{}) {}\n"

        self.generate_cli()

        #Should we continue to display the prompt? Set to False to stop.
        self.continue_session = True


    def generate_cli(self):
        """
        Generate the CLI. Updates class attributes cli_options, cli_prompt.
        :param cli_functions: List of functions that will be the CLI options
        :return: None
        """
        options = [i.__name__ for i in self.cli_functions]
        options = [i.replace("_", " ").title() for i in options]

        # Humans like to start from 1. Add 1 to the index so we start at 1 rather than 0.
        cli_options = [self.cli_options_template.format(options.index(i) + 1, i) for i in options]

        self.cli_options = cli_options

        cli_prompt = self.cli_message
        for option in cli_options:
            cli_prompt += option

        self.cli_prompt = cli_prompt


    def display_prompt(self):
        """
        Display the generated CLI prompt
        :return: None
        """
        if self.continue_session:

            print(self.cli_prompt)
            return self.continue_session

        else:
            return self.continue_session

    def add_option(self, function):
        """
        Wrapper to add a function to CLI. Re-generates the prompt and updates cli_options param.
        Designed to be used as a decorator.
        :param function: function object
        :return: None
        """
        # Make sure that quit() is always the last function.
        self.cli_functions.remove(self.quit)
        self.cli_functions.append(function)
        self.cli_functions.append(self.quit)
        self.generate_cli()

    def quit(self):
        """
        Leave the program.
        :return: None
        """

        self.continue_session = False


cli = CLI()

@cli.add_option
def send_message():
    pass

@cli.add_option
def add_donor():
    pass

@cli.add_option
def generate_report():
    pass


if __name__ == '__main__':

    while cli.display_prompt():

        x = input('Hey there :')
        print(x)

        if x == '3':
            cli.quit()