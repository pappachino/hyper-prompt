import os
from ..segment import BasicSegment


class Segment(BasicSegment):
    def activate(self):
        env = (self.getenv('VIRTUAL_ENV') or
               self.getenv('CONDA_ENV_PATH') or
               self.getenv('CONDA_DEFAULT_ENV'))
        if (self.getenv('VIRTUAL_ENV') and os.path.basename(env) == '.venv'):
            env = os.path.basename(os.path.dirname(env))
        if not env:
            return
        env_name = os.path.basename(env)
        bg = self.theme.get("VIRTUAL_ENV_BG")
        fg = self.theme.get("VIRTUAL_ENV_FG")
        self.append(" %s " % env_name, fg, bg)