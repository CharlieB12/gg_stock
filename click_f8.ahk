#Requires AutoHotkey v2.0

DllCall("SetProcessDPIAware") ; fix DPI scaling

WinActivate("Roblox")          ; change "Roblox" to your actual window title
WinWaitActive("Roblox", 5)     ; wait up to 5 seconds to get focus

Sleep(300)                    ; small delay for stability

MouseMove(657, 607)
Click()

