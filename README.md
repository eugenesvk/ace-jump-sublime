# AceJump

A plugin for Sublime Text 3 heavily inspired by AceJump for emacs.

AceJump allows you to move the cursor to any character to any place currently on screen.
To clarify, you can jump between characters in all visible portions of currently open documents in any panes.
Like it's emacs counterpart, AceJump for sublime features word (on the image below), character and line modes which make jumping even easier.

![AceJump](https://cloud.githubusercontent.com/assets/8056203/10858871/92069504-7f58-11e5-8593-e373121fd917.gif)

After selecting a mode, you type in a character (except in line mode, where you don't have to type in anything) and appropriate labels are displayed. Then all you need to do is press the key from the label and voila!

## Installation

### PackageControl

You can install AceJump from [PackageControl](http://wbond.net/sublime_packages/package_control) by following the steps below:

- Open up the command palette and select ```Package Control: Install Package```
- Wait for the packages index to load and select ```AceJump```

### Manual installation

You can install AceJump manually using git by running the following command within sublime packages directory (Preferences > Browse Packages):

```
$ git clone git@github.com:ice9js/ace-jump-sublime.git AceJump/
```

Or you can just copy the contents of this repository into ```Packages/AceJump```.

## Usage

### Word mode

Goes to a word starting with the given character. This mode works only with alphanumeric characters. If you're interested in jumping to a special character, use character mode instead.

- ```Ctrl/Super + Shift + ;```
- ```<head character>```
- ```<label>```

No need to press enter after selecting a label!

![Word mode](https://cloud.githubusercontent.com/assets/8056203/10858875/921aa814-7f58-11e5-99ec-9d17fc22f313.gif)

### Character mode

Goes to an occurence of the given character.

- ```Ctrl/Super + Shift + '```
- ```<character>```
- ```<label>```

![Character mode](https://cloud.githubusercontent.com/assets/8056203/10858870/92021b8c-7f58-11e5-916f-8ebc2d1d5eb4.gif)

### Line mode

Labels all non-empty lines and lets you jump to one of them.

- ```Ctrl/Super + Shift + .```
- ```<label>```

![Line mode](https://cloud.githubusercontent.com/assets/8056203/10858872/9207c596-7f58-11e5-9353-2d57783ca2cc.gif)

### Within Line mode

Labels all words within the line where current cursor locate and lets you jump to one of them.

- ```Ctrl/Super + Shift + ,```
- ```<label>```

### Select mode

After triggering select mode, the next jump will select everything inbetween the current cursor position and the selected label.
When select mode is triggered, the next jump is limited to the current file.

- ```Alt+;``` (```Ctrl+;``` for OS X)
- perform a jump using word, character or line mode

![Select mode](https://cloud.githubusercontent.com/assets/8056203/10858874/921207a4-7f58-11e5-936a-6e56ec80d486.gif)

### Multiple cursors mode

After triggering multiple cursors mode, the next jump will add a new cursor to the view instead of moving the existing one.
Again, when this mode is triggered, only jumps in the same file are available.

- ```Alt+'``` (```Ctrl+'``` for OS X)

![Multiple cursors mode](https://cloud.githubusercontent.com/assets/8056203/10858873/9207ee86-7f58-11e5-9251-e74bd64dbfed.gif)

### Jump-after mode

In this mode, the cursor will jump behind the targeted instance. Unfortunetely,
this mode cannot be paired with select or multiple cursors mode yet.

- ```Alt+.``` (```Ctrl+.``` for OS X)

![Jump-after mode](https://cloud.githubusercontent.com/assets/8056203/10858868/91fb4b22-7f58-11e5-8bdf-b489c6bb7ee2.gif)

### Batching

In case there are more places to jump to than labels available, labels will be batched and you can cycle through them by simply pressing enter.

![Batching](https://cloud.githubusercontent.com/assets/8056203/10858869/92006792-7f58-11e5-9ece-6b94d1016147.gif)

## Customization

In order to access AceJump settings, go to ```Preferences > Package Settings > AceJump > Settings - User``` or open command palette commands:

  - `Preferences: AceJump Settings` to open default and user settings side-by-side
  - `Preferences: AceJump Settings: Default`
  - `Preferences: AceJump Settings: User`
  - `Preferences: AceJump Keybinds: Default` to open default and user (common `Default (OSX).sublime-keymap` file, not AceJump-specific) keybinds side-by-side
  - `Preferences: AceJump Keybinds: User`
  - `Preferences: AceJump Keybinds`

### Key bindings

Default keybindings are disabled to avoid conflicts with your other keybinds, you can enable them by adding __either__ of the following settings to your `Preferences.sublime-settings` file via `Preferences: Settings` command palette command (NOT `AceJump.sublime-settings`):

  - `"ace_jump_key_single":true,`	every command mapped to a single key combo
  - `"ace_jump_key_chain" :true,`	<kbd>⌃</kbd><kbd>j</kbd> as a prefix key (<kbd>⌘</kbd> on a Mac) with letter-based "mnemonics" like `W`ord
  - `"ace_jump_key_chome" :true,`	<kbd>⌃</kbd><kbd>j</kbd> as a prefix key (<kbd>⌘</kbd> on a Mac) with more convenient home-row based locations

| Command                	| Single                               	| Chain                                             	| CHome                                                                                                                           	|
|------------------------	|--------------------------------------	|-------------------------------------------------- 	|-----------------------------------------------------------------------------------------------------------------------------    	|
| `ace_jump_word`        	| <kbd>⇧</kbd><kbd>⌃</kbd><kbd>;</kbd> 	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>w</kbd>	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>k</kbd>                                                                              	|
| `ace_jump_char`        	| <kbd>⇧</kbd><kbd>⌃</kbd><kbd>'</kbd> 	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>c</kbd>	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>l</kbd>                                                                              	|
| `ace_jump_line`        	| <kbd>⇧</kbd><kbd>⌃</kbd><kbd>.</kbd> 	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>l</kbd>	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>;</kbd>                                                                              	|
| `ace_jump_within_line` 	| <kbd>⇧</kbd><kbd>⌃</kbd><kbd>,</kbd> 	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>i</kbd>	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>j</kbd>                                                                              	|
| ↓ Modes                	|                                      	|                                                   	|                                                                                                                                 	|
| `ace_jump_add_cursor`  	| <kbd>⎇</kbd><kbd>'</kbd>             	| <kbd>⌃</kbd><kbd>j</kbd>,             <kbd>c</kbd>	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>a</kbd>, <kbd>⌃</kbd><kbd>k</kbd>[^1] or <kbd>l</kbd> or <kbd>;</kbd> or <kbd>j</kbd>	|
| `ace_jump_select`      	| <kbd>⎇</kbd><kbd>;</kbd>             	| <kbd>⌃</kbd><kbd>j</kbd>,             <kbd>s</kbd>	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>s</kbd>, <kbd>⌃</kbd><kbd>k</kbd>[^1] or <kbd>l</kbd> or <kbd>;</kbd> or <kbd>j</kbd>	|
| `ace_jump_after`       	| <kbd>⎇</kbd><kbd>.</kbd>             	| <kbd>⌃</kbd><kbd>j</kbd>,             <kbd>a</kbd>	| <kbd>⌃</kbd><kbd>j</kbd>, <kbd>⌃</kbd><kbd>f</kbd>, <kbd>⌃</kbd><kbd>k</kbd>[^1] or <kbd>l</kbd> or <kbd>;</kbd> or <kbd>j</kbd>	|

[^1]: instead of enabling a mode completes the sequence in one keybind

Or you can then override the bindings for any of the following commands via ```Preferences > Package Settings > AceJump > Key Bindings - User```:

- ```ace_jump_word```
- ```ace_jump_char```
- ```ace_jump_line```
- ```ace_jump_within_line```
- ```ace_jump_select```
- ```ace_jump_add_cursor```
- ```ace_jump_after```

The commands accept an optional Boolean `current_buffer_only` argument. When present and set to `true`, AceJump only performs on the currently edited buffer.

### Labels

You can override the ```labels``` setting to provide your own set of labels to be used by AceJump.

### Indicators

When invoking 3 mode commands (`ace_jump_select`, `ace_jump_add_cursor`, and `ace_jump_after`) you can have visual indicators that a mode is on via a popup menu (e.g., when selection is on you'd see a ▋ symbol ![popup](./img/popup.png)) or in the statubar by setting `popup_mode` and `status_mode` settings. There are also additional settings for more control of these indicators, see `Preferences: AceJump Settings: Default`

### Highlighting

You can also set the syntax scope that's used for highlighting by overriding ```labels_scope```. The default scope is ```invalid```. Also you can set the syntax scope for the carets via the `inactive_carets_scope` setting, e.g., `""` blank would hide the carets when labels are shown.

### Case sensitivity

Ace jump is case sensitive by default. Case sensitivity can be toggled on and off by altering the ```search_case_sensitivity``` setting.

### Jumping behind the last character in a line

By setting ```jump_behind_last_characters``` to ```true```, AceJump will jump behind a character if it's the last character on a line, without the need to trigger jump after mode. This only works in character mode and is switched off by default.

### Theme

AceJump changes the theme to a blank one when labels are shown to make them more visible, by setting `change_theme` to `false` you can disable this. 

### Known issues

It has been reported that the _Select mode_, _Multi cursors mode_ and _Jump after_ mode might not work using the specified keybinding.  
As a workaround for that follow these steps:

- Start a regular search, e.g. word search (default keybinding: Ctrl+Shift+;).
- **Before** entering any character, activate the advanced mode (e.g. for _Select mode_ use Alt+;).
- Now enter the character to lookup.
- Use the label to go to the corresponding location.
