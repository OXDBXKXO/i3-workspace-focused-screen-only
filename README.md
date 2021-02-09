# i3-workspace-focused-screen-only

When using multiple screens in i3, workspace numbers are shared, causing workspace prev and next commands to switch focus from one display to another.

This script allows switching to previous and next workspaces on the focused screen only, which is the behaviour you expect when using tools like [fusuma](https://github.com/iberianpig/fusuma).

To use it, `chmod +x` it and update `workspace prev`and`workspace next`occurences in i3 config file to use the script instead (with`prev`or`next` as parameter).

**Example:**

```
#bindsym $mod+Control+Left workspace prev
bindsym $mod+Control+Left exec --no-startup-id "~/scripts/focused-workspace-only.py prev"
```
