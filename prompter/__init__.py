class Prompter:

    """ My Cmd class for preprocessing the Python interpreter"""

    DEFAULT_PROMPT = ">>> "
    DEFAULT_INTRO = "Welcome to Prompter!\n"

    def __init__(self, stdin = None, stdout = None, prompt = None, intro = None):
        self.stdin = stdin
        self.stdout = stdout
        self.prompt = prompt if prompt is not None else DEFAULT_PROMPT
        self.intro = intro if intro is not None else DEFAULT_INTRO
        
    def readline(self):
        """ Read a line from specified stdin """

        return self.stdin.readline()
    def print(self, *args, **kwargs):
        """ Print to specified stdout """

        print(*args, **kwargs, file = self.stdout)

    def prompt_input(self):
        """ Get input from user using specified prompt """

        self.print(self.prompt, end = '')
        return self.readline()

    """ Methods for subclass implementation """
    def pre_prompt(self):
        pass
    def on_prompt(self, line):
        pass
    def post_prompt(self):
        pass

    def cmdloop(self):
        while True:
            self.pre_prompt()
            line = self.prompt_input()
            exit_flag = self.on_prompt(line)
            self.post_prompt()
            if exit_flag:
                break
