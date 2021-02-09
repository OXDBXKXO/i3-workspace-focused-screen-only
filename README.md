# i3-workspace-multi-screen

When using multiple screens in i3, workspace numbers are shared, causing workspace prev and next commands to switch focus from one displays to another.

This script allows switching to previous and next workspaces on the focused screen only, which is the behaviour you expect when using tools like [fusuma](https://github.com/iberianpig/fusuma).

To use it, just replace `workspace prev` and `workspace next` occurences by calls to the script (with `prev` or `next` as parameter).
