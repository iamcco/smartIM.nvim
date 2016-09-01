import os
import neovim

@neovim.plugin
class SmartIM(object):
    def __init__(self, vim):
        self.vim = vim
        self.default_input_method = "com.apple.keylayout.ABC"
        self.save_input_method = ''

    @neovim.autocmd('InsertLeave', pattern='*', eval="g:smart_im_select_exec_path")
    def auto_insert_leave(self, path):
        p = os.popen(path)
        self.save_input_method = p.read().strip()
        p.close()
        os.system(path + self.default_input_method)

    @neovim.autocmd('InsertEnter', pattern='*', eval="g:smart_im_select_exec_path")
    def auto_insert_enter(self, path):
        os.popen(path + self.save_input_method).close()

    @neovim.autocmd('VimLeavePre', pattern='*', eval="g:smart_im_select_exec_path")
    def auto_vim_leave_pre(self, path):
        os.popen(path + self.save_input_method).close()
