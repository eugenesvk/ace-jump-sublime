import re
import sublime, sublime_plugin

re_sp = re.compile(r'\s+')
DEF = dict(
   enable   	= True
  ,prefix   	= ''
  ,template 	= '''<body id="nv_motion_count"><span>{prefix}{count}</span></body>'''
  ,maxwidth 	= 80
  ,maxheight	= 30
)
import copy
CFG = copy.deepcopy(DEF) # copy defaults to be able to reset values on config reload

from sublime import active_window, PopupFlags
def get_popup_html(sym) -> str:
  return CFG['template'].format_map(dict(prefix=CFG['prefix'],count=sym))
def show_popup_mode(view:sublime.View, sym:str, point:int=-1) -> None:
  cfg = sublime.load_settings("AceJump.sublime-settings")
  if not cfg.get("popup_mode",False):
    return
  cfg_flag = re.split(re_sp,cfg.get("popup_flag","").lower())
  flags = PopupFlags.KEEP_ON_SELECTION_MODIFIED
  # todo: move ↓ to a loading function instead of parsing each time
  for key in [           "NONE"                        ,"no"    	]: #
    if key in cfg_flag:                                         	#
      flags |= PopupFlags.NONE                                  	#
  for key in [           "COOPERATE_WITH_AUTO_COMPLETE","acompl"	]: # Causes the popup to display next to the auto complete menu
    if key in cfg_flag:                                         	#
      flags |= PopupFlags.COOPERATE_WITH_AUTO_COMPLETE          	#
  for key in [           "HIDE_ON_MOUSE_MOVE"          ,"hmo"   	]: # Causes the popup to hide when the mouse is moved, clicked or scrolled
    if key in cfg_flag:                                         	#
      flags |= PopupFlags.HIDE_ON_MOUSE_MOVE                    	#
  for key in [           "HIDE_ON_MOUSE_MOVE_AWAY"     ,"hma"   	]: # Causes the popup to hide when the mouse is moved (unless towards the popup), or when clicked or scrolled
    if key in cfg_flag:                                         	#
      flags |= PopupFlags.HIDE_ON_MOUSE_MOVE_AWAY               	#
  for key in [           "KEEP_ON_SELECTION_MODIFIED"  ,"ksel"  	]: # Prevent the popup from hiding when the selection is modified 4057
    if key in cfg_flag:                                         	#
      flags |= PopupFlags.KEEP_ON_SELECTION_MODIFIED            	#
  for key in [           "HIDE_ON_CHARACTER_EVENT"     ,"hc"    	]: # Hide the popup when a character is typed 4057
    if key in cfg_flag:                                         	#
      flags |= PopupFlags.HIDE_ON_CHARACTER_EVENT               	#

  if sym:
    view.show_popup(
       content   	= get_popup_html(sym)	# str
      ,flags     	= flags              	#
      ,location  	= point              	# Point -1
      ,max_width 	= CFG['maxwidth']    	# DIP
      ,max_height	= CFG['maxheight']   	# DIP
    )
  else:
    view.hide_popup()
