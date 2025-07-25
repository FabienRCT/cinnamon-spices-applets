### v7.9.0
  * Bugfix about themes.
  * Added a “Check all the first boxes then refresh” button in each tab of this applet’s settings, except in the General tab.
  * Please note: when certain boxes remain unchecked, it means that these spices are not included in the Cinnamon database.

### v7.8.8~20250425
  * Fixes [#7090](https://github.com/linuxmint/cinnamon-spices-applets/issues/7090).

### v7.8.7~20250324
  * Adapts constants.js for themes.
  * Code cleanup.

### v7.8.6~20250323
  * Fixes #6992: Improves the appearance of the label in a horizontal panel.

### v7.8.5~20250315
  * BugFixes in a bash script.

### v7.8.4~20250304
  * Improved functioning.

### v7.8.3~20250303
  * Minor bugfix.

### v7.8.2~20250303
  * Does not try to translate null messages from other spices. This also helps avoid black screens.

### v7.8.1~20250302
  * Forces the use of 'cjs' even if 'gjs' is installed.
  * Uses “try” for each “destroy” command.
  * Fixes #6933.

### v7.8.0~20250215
  * Tooltip bug fixed.

### v7.7.0~20250211
  * Consider AlbumArt3.0@claudiux as a common desklet.

### v7.6.7~20250204
  * Avoids the use of Array.toString() in the code.

### v7.6.6~20250203
  * No more errors on restart.

### v7.6.5~20250202
  * Fixes #6776.
  * Code: No 'bind(this)' calls anymore.

### v7.6.4~20250131
  * Improves directory and file management.
  * Code clean-up.

### v7.6.3~20250130
  * Try to fix #6776.

### v7.6.2~20250126
  * Modification of the menu to fix #6781.

### v7.6.1~20250120
  * Fixes #6776.

### v7.6.0~20250119
  * Do not check private Spices. A private Spice is a Spice that is not listed on the Cinnamon Spices website.
  * Code: Avoids using Lang.bind() in response to signals.

### v7.5.3~20250116
  * mainloopTools library: improvements.

### v7.5.2~20250112
  * Fixed minor bugs in animations.

### v7.5.1~20250112
  * Now use mainloopTools to optimize loop management.

### v7.5.0~20250111
  * Improved management of loops.

### v7.4.7~20250105
  * Now compatible with Cinnamon on Gentoo.
  * Replaces apturl with xdg-open.
  * Lets the user enter commands when dependencies are missing.

### v7.4.6~20241230
  * Spices not selected in the lists of settings are displayed first.

### v7.4.5~20241114
  * Soup2/Soup3: better detection.

### v7.4.4~20240602
  * Restarts httpLib when network interface status changes.

### v7.4.3~20240531
  * Wait a few seconds before refreshing data after a change in network status.

### v7.4.2~20240805
  * Saves memory.

### v7.4.1~20240502
  * Fixes #5969: Wait 20 seconds before executing the cache update loop, so that mintupdate runs correctly.

### v7.4.0~20240423
  * Now smoother so as not to be blocked by the cinnamon-spices.linuxmint.com server.
  * New color when spices are updated or forgotten.
  * Translations: New .pot file. New fr.po file.
  * Seems to fix #5941.


### v7.3.7~20240421
  * Refresh action further improved.

### v7.3.6~20240420
  * Improved Refresh action.

### v7.3.5~20240420
  * Improved cache refresh management.

### v7.3.4~20240419
  * Prevents telescoping with mintupdate.
  * Uses G. Translate to display help.

### v7.3.3~20240416
  * Code cleanup.

### v7.3.2~20240415
  * Bugfixes.
  * Checks again after installing updates.

### v7.3.1~20240415
  * Takes into account the new location of themes.

### v7.3.0~20240413
  * Also manage Actions for nemo.
  * Fixes #5683.

### v7.2.0~20240412
  * Removes the "Update" button from notifications for the time being. It will be available again when cinnamon-settings is compatible.
  * Many bugfixes.
  * TODO: Include Nemo Actions.

### v7.1.2~20240412
  * Fixes definitively #5682: now this applet also works on distributions that don't use mintupdate.

### v7.1.1~20240412
  * Fixed a bug that prevented SpiceUpdate from starting.

### v7.1.0~20240411
  * Fixes #5682 and many other bugs.
  * TODO: Include Nemo Actions. Update all Spices of a given type.

### v7.0.0~20240411
  * Fixes #3773 #4584 #4850 #5167 #5216.
  * This version works with Cinnamon 6.0! Even if a few adjustments need to be made.

### v6.4.3~20231209
  * Fixes #5167. Use of Soup3 (Cinnamon 6.0).
.
### v6.4.2~20230413
  * Minor bugfix.


### v6.4.1~20230309
  * Now compatible with openSUSE.

### v6.4.0~20230217
  * Avoid to be blocked by the spices server.
  * Add 5.6 branch.

### v6.3.1~20201026
  * Adapting SpicesUpdate@claudiux to [cinnamon/9664](https://github.com/linuxmint/cinnamon/pull/9664#event-3912970920).

### v6.3.0~20201022
  * Tooltip content: Now filtered and formatted. Some information is displayed in bold, others in italics.
  * Settings (General tab): Possibility to define a maximum width for the content of the tooltip (in % of the screen width).
  * Badge: Size and location changed. Now the size of this applet remains constant, with or without its badge.
  * Network monitoring: Now continue to check for updates even if network has changed (VPN).
  * Some optimizations.

### v6.2.0~20201012
  * Improvements (for Cinnamon 4.6 only):
    * Settings: Changing the position of the Refresh button. Remove the buttons below the lists (for future Cinnamon).
    * Tooltip: Some information is displayed in bold.
    * Notifications: Some information is displayed in bold.
    * Animation: Adding linear effect.

### v6.1.0~20201011
  * Fix issue #3253

### v6.1.0~20201010
  * For Cinnamon 4.6 only:
    * Now detects when the Cinnamon server is down.
    * Bug fixes.
    * No longer displays "Spices Update" or "SpU" next to or below the icon.

### v6.0.2~20200811
  * Remove all notifications when reloading this applet.
  * Menu shows the "reload this applet" option when a RELOAD file exists at the root of this applet.

### v6.0.1~20200806

"Weight" reduction of this applet: the `Symbola` font is no longer included in its package; it was only used for Arch and the `install_symbola_on_Arch.sh` script was modified to download it if needed.

### v6.0.0~20200729

Many improvements, only for Cinnamon 4.2 and following.

  * Spices Update automatically adapts the verification or not of each type of Spices (for example: it does not check the themes if no theme is installed; it checks them as soon as at least one theme is installed). However, the user is always free to decide, in settings, what should be done.

  * Checking for new Spices is now disabled by default.

  * New option in General Settings: "Show the 'Update All' button in notifications" (with buttons). For example, clicking on this button in a notification for available Themes updates:
    1. opens the Download tab of System Settings about Themes,
    2. refreshes the cache about Themes,
    3. downloads and install all latest updates for your Themes.
    4. When all updates are made, just close yourself this System Settings window.

  * New button 'Forget' in notifications about new Spices.
  * The applet icon now rotates during the entire refresh process.
  * Displays a notification asking the user to check the applet settings, if this is the first installation of this version of Spices Updates. This notification only appears once.
  * Better management of notifications. Spices Update does not use notify-send anymore.
  * Help button (in menu) shows in the browser by default an approximate translation of the web page: https://cinnamon-spices.linuxmint.com/applets/view/309

### v5.4.2~20200615
  * Bug fixes

### v5.4.1~20200613
  * Code cleanup
  * Now displays the badge showing the number of updates only after all checks have been completed.

### v5.4.0~20200608
  * Now compatible with Cinnamon 4.6.
  * Fixes #2927, #2972, #3020.

### v5.3.0~20200209
  * Cinnamon 4.2 & 4.4: Direct access from the Spices Update menu to each tab of settings (General, Applets, Desklets, Extensions, Themes) via the Configure sub menu.

### v5.2.2~20200109
  * Cinnamon 4.2: Let Gtk determine the right size of dialog window ([see @mtwebster's commit for Cinnamon](https://github.com/linuxmint/cinnamon/commit/d57677b5ae306115139be98be62e3fb7cc6a27a8#diff-c4641b580bb45b188c5ae94c7f7a33cf))

### v5.2.1~20191230
  * Make it configurable for Cinnamon 2.8 -> 4.0.

### v5.2.0~20191124
  * Cinnamon 4.4: Use Xapp widgets and speed up loading of the icon for the icon theme widget. (Thanks to collinss.)
  * Cinnamon 4.3: Removed (now useless).

### v5.1.3~20191118
  * Cinnamon 4.4: replaces the cgi module by the html one to be compatible with Python 3.8 (used on Arch).

### v5.1.2~20191117
  * Translations: Updates files: .pot, fr.po and es.po.

### v5.1.1~20191116
  * Now compatible with Python 3.8 (used on Arch)
  * Now can sort Spices by 'update' (Cinnamon 4.2)

### v5.1.0~20191114
  * Closes #2679.
  * Closes #2680.
  * Closes #2681.

### v5.0.0~20191105

Many new features and improvements.

  * Compatible with Cinnamon 4.4.
  * For Cinnamon 4.4: Uses the new sort by 'Upgradable' in the Download tab of System Settings for Applets, Desklets, Extensions and Themes. This sort shows the upgradable Spices first, then acts as the sort by date. Thanks to Clément Lefebvre for embedding my code in Cinnamon 4.4.
  * Adds for Cinnamon 3.8 and 4.0 the ability, already present for Cinnamon 4.2, to renew the download of the latest version of a Spice.
  * For Cinnamon 3.8 and greater:
    * Spices you do not want to upgrade (as you defined in this applet's Settings) do not anymore appear as upgradable in the Download tab of System Settings for Applets, Desklets, Extensions and Themes, even if updates are available for them. This avoids unfortunate updates and allows to confidently use the 'Update All' button.
  * Fixes icon size bug in Hi-DPI mode.

### v4.5.0~20191028
  * Animated icon during refresh.
    * For Cinnamon 3.8 and greater.

### v4.4.0~20191022
  * Middle-Click on applet icon:
    * Performs a Refresh while no available updates are reported.
    * Opens all useful Cinnamon Settings, when Spices updates are available, to allow the user to perform these updates.

### v4.3.0~20191020
  * Better behavior when many spices need updating.
  * Take better account of manually installed spices.

### v4.2.1~20191004
  * Adds the ability to increase up to 720 hours (30 days) the time between two checks. (User request.)

### v4.2.0~20190927
  * Animated icon during refresh.
    * Only for Cinnamon 4.2 and following.

### v4.1.0~20190925
  * Adds the ability to renew the download of the latest version of a Spice.
    * Only for Cinnamon 4.2 and following.
  * `SpicesUpdate@claudiux.pot` file updated.
  * French translation: `fr.po` file updated.
  * Minor bugs fixed.

### v4.0.2~20190920
  * Removes unnecessary notifications like '(Refresh to see the description)'.
  * Minor CSS changes.

### v4.0.1~20190914
  * Improves the download of the latest versions of Spices. (Cinnamon 3.8 and following.)

### v4.0.0~20190912
  * Make sure to download the latest version of Spices. (Cinnamon 3.8 and following.)

### v3.2.0~20190910
  * Improves tooltip display. (All branches)
  * Bug fixes in the 2.8 branch. (Cinnamon from 2.8 to 3.6)
  * Code cleanup and restructuring in the 4.2 branch. (Cinnamon 4.2 and following.)

### v3.1.0~20190908
  * Multi-version: Using specific capabilities of `cinnamon-settings` in Cinnamon 4.2.
  * Code cleanup.

### v3.0.4~20190826
  * Available languages:
   * Dutch
   * English
   * Finnish
   * French
   * Italian
   * German
   * Hungarian
   * Spanish
   * Swedish.
  * Bug (#2545) fixed concerning Cinnamon 2.8 -> 3.6.

### v3.0.3~20190818
  * Improves installation.
  * Removes useless log messages.

### v3.0.2~20190813
  * Show Spices Update version in tooltip

### v3.0.1~20190812
  * Fixes notification button issue (#2360)

### v3.0.0~20190808
  * Now compatible with Cinnamon 2.8 -> 4.2 (Mint 17.3 -> 19.2)!
   * From Cinnamon 3.8 to 4.2 (Mint 19 -> 19.2): Perfectly functional, as usual.
   * From Cinnamon 2.8 to 3.6 (Mint 17.3 -> 18.3): Some features are reduced:
    * The Spices configuration window does not open on the second tab, only on the first one. You will need to click on the second tab and select the sort by date yourself.
    * The Settings window of this applet does not contain any tabs.
    * In the settings of this applet, you can not access Spices lists to disable their monitoring. Therefore, all installed Spices are monitored.
    * The script `generate_mo.sh` (in the `scripts` folder) allows you to install all available translations. Restart Cinnamon after execution.
    * If the `Symbola_Hinted` font can not be automatically installed, then place you into the `fonts/symbola` folder and double-click on the `Symbola_Hinted.ttf` file. Install it with the just opened `gnome-font-viewer`.
    * Cinnamon 2.8: The number of changes does not appear next to the Spices Update icon.
  * The Eye character signaling the new Spices is replaced by a Comet character.

### v2.3.1~20190807
  * Minor change: Replaces, in tooltip and in notifications, escaped characters \' and \" by ' and ", if any.

### v2.3.0~20190806
  * Bypass all caches to download json files containing data about Spices.

### v2.2.0~20190803
  * Adding a "Help..." button in the menu. This help (in English by default) can be translated into your language. To do it:
   * Place you into the `help` directory: `cd ~/.local/share/cinnamon/applets/SpicesUpdate@claudiux/help`
   * Copy the `en` directory into a new directory named as your language code. Example: `cp -a en de`
   * Place you into this new directory. Translate the contents of the README.md file. (Do not rename this file.)
   * Install the `grip` package, then export the README.md file into html format: `grip --title "Spices Update - Help" --export README.md README.html`. (Translate _Help_.)
   * You can propose your translation, mentionning me (@claudiux) on Github.
  * French translation of the README.md file is available.
  * When only one Spice (by category: Applets, Desklets, ...) needs an update, its icon appears into the notification messages.

### v2.1.0~20190721
  * Allows user to update even downloaded xlets from the Download button on the site.
  * Compatible with Cinnamon 3.8, 4.0 and 4.2.

### v2.0.1~20190201
  * Delete old notifications when a new one arrives.

### v2.0.0~20190131
  * Now the notifications can contain a button to open Download page for applets/desklets/extensions/themes in Date sort order. (Feature request #2231.)
  * Now the notifications can contain the description of an update or new Spice. (Feature request #2243.)
  * If the Symbola font is not already installed on Arch, then its installation is now made locally (into `~/.local/share/fonts/`) to avoid using AUR repositories, which are not used on all Arch system.

### v1.2.1~20190126
  * The icon applet can be hidden while nothing is to report.

### v1.2.0~20190122
  * Now, in the menu, a click on a type of Spice (Applets, Desklets, etc) opens the Download tab of the corresponding page in Cinnamon Settings, with Spices sorted by date.

### v1.1.3~20190118
  * Dependencies: Added presence of `symbola` ttf font.

### v1.1.2~20190117
  * New feature (requested by @sphh in #2210): Make support for new Spices Applet, Desklet, Extension and Theme specific.

### v1.1.1~20190115
  * New feature (requested by @sphh in #2213): When new Spices are available, an option _Forget new Spices_ appears in the menu of this applet. Clicking it will clear these notifications of new spices, until others arrive.
  * Available languages: English, French, Spanish, Croatian, German, Italian.

### v1.1.0~20190113
  * New feature (requested by @sphh in #2202): This applet can also warn the user when new Spices are available. (New option in general settings.)
  * Minor bug fixes.

### v1.0.4~20190110
  * New icons. Back to the original color: #eb9122.
  * The tooltip now contains the list of Spices to update.
  * Fixes undeclared variable error.

### v1.0.3~20190107
  * New icons.
  * Detects the default symbolic-icon color from the current theme.
  * Change the default color of the icon when spices need updates. This does not affect the choice made by the user.
  * Available languages: English, French, Spanish, Croatian, German.

### v1.0.2~20190104
  * Configure button added in menu, to open the settings.
  * Refresh button added in the settings, on each spice panel (applets, desklets ...) to force the refresh of the list.
  * Improved list refresh.
  * Make this applet icon resizable. (Fixes #2180)
  * Available languages: English, French, Spanish, Croatian.

### v1.0.1~20190103
  * Better management of notification messages.
  * A new option allows the user to choose whether identical messages are displayed or not.
  * SpicesUpdate@claudiux.pot updated.
  * Available languages: English, French, Spanish.

### v1.0.0~20190102
  * Fully functional.
  * Tested on Cinnamon 4.0.8 (Linux Mint 19.1 & Antergos (Arch) Linux).
  * Tested on Cinnamon 3.8.9 (Fedora 27).
  * Available languages: English, French.
