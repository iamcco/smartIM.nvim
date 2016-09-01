" vim:set et sw=4 ts=4 fdm=marker fdl=1:
" author: 年糕小豆汤 <ooiss@qq.com>
" update: 2016/09/01

if !exists('g:start_im_nvim')
    let g:start_im_nvim = 1
else
    finish
endif

let g:smart_im_select_exec_path = expand('<sfile>:p:h') . '/im-select '

