class Prompter:

    """ My Cmd class for preprocessing the Python interpreter"""

    def __init__(self, stdin = None, stdout = None, prompt = None, intro = None, outro = None):
        self.stdin = stdin
        self.stdout = stdout
        self.prompt = prompt if prompt is not None else ">>> "
        self.intro = intro if intro is not None else "Welcome to Prompter!\n"
        self.outro = outro if outro is not None else ""
        
    def readline(self):
        """ Read a line from specified stdin """
        if self.stdin is not None:
            return self.stdin.readline()
        else:
            return input()
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
    def on_eof(self) -> bool:
        return False
    def on_prompt(self, line: str) -> bool:
        return True
    def post_prompt(self):
        pass

    def cmdloop(self):
        self.print(self.intro)
        while True:
            self.pre_prompt()
            try:
                line = self.prompt_input()
                ok_flag = self.on_prompt(line)
            except EOFError:
                ok_flag = self.on_eof()
            self.post_prompt()
            if ok_flag is not None and not ok_flag:
                self.print(self.outro)
                break
