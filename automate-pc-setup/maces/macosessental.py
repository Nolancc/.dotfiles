import os
import keyboard
import time
def run():
    password = input("please enter sudo password: ")
    os.system("touch ~/jsfhd.txt")
    pwdfile = open("~/jsfhd.txt","w")
    pwdfile.write(password)
    pwdfile.close()
    os.system('zsh ~/automate-pc-setup/maces/call-brew.sh')
    print("installing brew")
    os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    os.system("echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/$USER/.zprofile")
    os.system("eval $(/opt/homebrew/bin/brew shellenv)")
    time.sleep(3)
    os.system("brew install appcleaner")
    time.sleep(3)
    os.system("brew install IINA")
    time.sleep(3)
    os.system("brew install rectangle")
    time.sleep(3)
    os.system("brew install dockutil")
    time.sleep(3)
    time.sleep(5)
    os.system("dockutil --remove Maps")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Photos")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove FaceTime")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove TV")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Music")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Downloads")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove News")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Calendar")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Reminders")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Contacts")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Notes")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Freeform")
    time.sleep(5)
    print("done")
    os.system("dockutil --remove Messages")
    time.sleep(5)
    print("done")
    os.system("defaults write com.apple.dock mineffect -string scale && killall Dock")
    time.sleep(3)
    os.system("defaults write com.apple.dock show-recents -bool false && killall Dock")
    time.sleep(3)
    os.system("defaults write com.apple.dock tilesize -int 40 && killall Dock")
    time.sleep(3)
    os.system("defaults write NSGlobalDomain AppleShowAllExtensions -bool true && killall Finder")
    time.sleep(3)
    pwdfile = open("~/Library/Preferences/com.knollsoft.Rectangle.plist","w")
    pwdfile.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>NSNavLastRootDirectory</key>
	<string>~/Documents</string>
	<key>NSNavPanelExpandedSizeForOpenMode</key>
	<string>{800, 448}</string>
	<key>NSWindow Frame NSNavPanelAutosaveName</key>
	<string>773 645 430 195 0 0 1920 1055 </string>
	<key>SUEnableAutomaticChecks</key>
	<false/>
	<key>SUHasLaunchedBefore</key>
	<true/>
	<key>allowAnyShortcut</key>
	<false/>
	<key>alternateDefaultShortcuts</key>
	<true/>
	<key>gapSize</key>
	<real>0.0</real>
	<key>hideMenubarIcon</key>
	<true/>
	<key>landscapeSnapAreas</key>
	<string>null</string>
	<key>lastVersion</key>
	<string>82</string>
	<key>launchOnLogin</key>
	<true/>
	<key>portraitSnapAreas</key>
	<string>null</string>
	<key>reflowTodo</key>
	<dict>
		<key>keyCode</key>
		<integer>45</integer>
		<key>modifierFlags</key>
		<integer>786432</integer>
	</dict>
	<key>subsequentExecutionMode</key>
	<integer>1</integer>
	<key>toggleTodo</key>
	<dict>
		<key>keyCode</key>
		<integer>11</integer>
		<key>modifierFlags</key>
		<integer>786432</integer>
	</dict>
</dict>
</plist>
''')
    pwdfile.close()
    os.system("rm  ~/jsfhd.txt")
    print('''setup complete
          reboot mac to apply all changes''')
