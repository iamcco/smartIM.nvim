import os
import neovim

@neovim.plugin
class SmartIM(object):
    def __init__(self, vim):
        self.vim = vim
        self.smart_im_select_command = ''
        self.smart_im_default_method = ''
        self.smart_im_save_status = ''
        self.isinited = False
        self.ismac = False

    @neovim.function('SmartIM2en')
    def insert_leave(self, args):
        if (not self.isinited):
            self.init_data()

        if (self.ismac):
            self.insert_leave_mac()
        else:
            self.insert_leave_linux()

    @neovim.function('SmartIM2save')
    def insert_enter(self, args):
        if (self.isinited):
            if (self.ismac):
                self.insert_enter_mac()
            else:
                self.insert_enter_linux()

    def init_data(self):
        self.smart_im_select_command = self.vim.eval('g:smart_im_select_command')
        self.smart_im_default_method = self.vim.eval('g:smart_im_default_method')
        self.ismac = self.vim.eval('g:smart_im_is_mac') == '1'
        self.isinited = True

    def insert_leave_linux(self):
        p = os.popen(self.smart_im_select_command)
        self.smart_im_save_status = p.read().strip()
        p.close()
        if (self.smart_im_save_status == '2'):
            os.popen(self.smart_im_select_command + self.smart_im_default_method).close()

    def insert_leave_mac(self):
        p = os.popen(self.smart_im_select_command)
        self.smart_im_save_status = p.read().strip()
        p.close()
        if (self.smart_im_save_status != self.smart_im_default_method):
            os.popen(self.smart_im_select_command + self.smart_im_default_method).close()

    def insert_enter_linux(self):
        if (self.smart_im_save_status == '2'):
            os.popen(self.smart_im_select_command + '-o').close()

    def insert_enter_mac(self):
        if (self.smart_im_save_status != self.smart_im_default_method):
            os.popen(self.smart_im_select_command + self.smart_im_save_status).close()

