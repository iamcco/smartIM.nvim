" vim:set et sw=4 ts=4 fdm=marker fdl=1:
" author: 年糕小豆汤 <ooiss@qq.com>
" update: 2016/09/19

if !exists('g:smart_im_nvim')
    let g:smart_im_nvim = 1
else
    finish
endif

if has('mac')
    let g:smart_im_select_command = expand('<sfile>:p:h') . '/im-select '
    let g:smart_im_default_method = 'com.apple.keylayout.ABC'
else
    let g:smart_im_select_command = 'fcitx-remote '
    let g:smart_im_default_method = '-c'
endif

let g:smart_im_is_mac = has('mac')

autocmd InsertLeave * call SmartIM2en()
autocmd InsertEnter * call SmartIM2save()
autocmd VimLeavePre * call SmartIM2save()

