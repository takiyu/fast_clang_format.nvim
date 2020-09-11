import neovim

import subprocess

# -----------------------------------------------------------------------------
# --------------------------------- Constants ---------------------------------
# -----------------------------------------------------------------------------
CLANG_FORMAT_CMD = 'clang-format'


# -----------------------------------------------------------------------------
# ----------------------------------- Plugin ----------------------------------
# -----------------------------------------------------------------------------
@neovim.plugin
class FastClangFormatPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('FastClangFormat', sync=True, nargs='?')
    def make_split_comment(self, args):
        # Obtain full path of the current filename
        filename = self.nvim.eval("expand('%:p')")
        # Apply clang-format
        subprocess.call([CLANG_FORMAT_CMD, '-i', filename])
        # Open again
        self.nvim.command(f'edit {filename}')

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
