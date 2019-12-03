#!/usr/bin/env python3

# TODO Add function or child class for sub-prompts

class CLI():
    """
    Class to present a CLI to the user.
    """

    def __init__(self, cli_functions=None):
        """
        Initialize the CLI class.
        :param cli_functions: Optionally pass in a list of functions at instantiation.
        """
        if cli_functions is None:
            cli_functions = []
        cli_functions.append(self.quit)  # Add quit() to our probably empty list of functions
        self.cli_functions = cli_functions
        self.cli_message = ("Menu Options\n")
        self.cli_options_template = "{}) {}\n"

        # Generated with helper function generate_cli
        self.cli_prompt = None
        self.cli_options = None

        self.generate_cli()

        # Should we continue to display the prompt? Set to False to stop.
        self.continue_session = True

    def generate_cli(self):
        """
        Generate the CLI. Updates class attributes cli_options, cli_prompt.
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

    def run_cli(self):
        """
        Display the CLI to the user and prompt for input.
        :return: None
        """

        def get_function():
            """
            Helper function to  return the function to run based on the option selected.
            :return: Function object.
            """

            try:
                user_input = input('Please select option: ')
            except KeyboardInterrupt:
                return self.quit

            # Did we get an option number?
            try:
                user_input = int(user_input)
                function_index = user_input

            except ValueError:  # We got a string. Check if it's a valid option.
                lowercase_options = [i.lower().replace('\n', '')[3:] for i in self.cli_options]

                if user_input.lower() in lowercase_options:
                    function_index = lowercase_options.index(user_input) + 1  # Because we added 1 to the options index

                else:
                    print("Invalid selection.\n\n")
                    return get_function()

            try:
                selected_function = self.cli_functions[function_index - 1]  # Remove that 1 we added earlier
                return selected_function

            except IndexError:
                print("Invalid selection.\n\n")
                return get_function()

        while self.display_prompt():
            function = get_function()
            function()

    @staticmethod
    def subprompt():
        """
        Present a subprompt. Should be called from within
        functions wrapped by @add_option.
        :return: User input string
        """

        pass



