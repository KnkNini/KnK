$allWindows = `lsUI -windows`; 
for ($window in $allWindows)
{
if ($window != "CommandWindow" && $window != "ConsoleWindow" && $window != "MayaWindow" && $window != "nexFloatWindow")
{
deleteUI $window;
}
};