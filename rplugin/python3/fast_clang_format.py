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

    @neovim.command('FastClangFormat', sync=True, nargs=0)
    def apply_clang_format(self):
        self._impl()

    @neovim.command('FastClangFormatAsync', sync=False, nargs=0)
    def apply_clang_format_async(self):
        self._impl()

    def _impl(self):
        # Obtain full path of the current filename
        filename = self.nvim.eval("expand('%:p')")
        # Apply clang-format
        subprocess.call([CLANG_FORMAT_CMD, '-i', filename])
        # Open again
        self.nvim.command(f'edit {filename}')

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
