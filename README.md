# i3-workspace-multi-screen

When using multiple screens in i3, you can use `workspace prev|next` to switch to prev|next workspace following workspaces numbers, and `workspace prev_on_output|next_on_output` to restrict the switch to the focused output only.

This script adds option to switch between outputs, which I personally use with [fusuma](https://github.com/iberianpig/fusuma).

**Available parameters:**

* `prev_num|next_num`: calls `i3-msg workspace prev|next`
* `prev_same_output|next_same_output`: calls `i3-msg workspace prev_on_output|next_on_output`
* `prev_output|next_output`: change focus to prev|next output
