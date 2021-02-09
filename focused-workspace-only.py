#! /usr/bin/python
import subprocess, json, sys

def getLayout():
    try:
        i3_workspaces_raw = subprocess.check_output(['i3-msg', '-t', 'get_workspaces'])
    except subprocess.CalledProcessError as err:
        print(err)
    i3_workspaces = json.loads(i3_workspaces_raw)

    try:
        i3_displays_raw = subprocess.check_output(['i3-msg', '-t', 'get_outputs'])
    except subprocess.CalledProcessError as err:
        print(err)
    i3_displays = json.loads(i3_displays_raw)

    layout = []
    focused = 0
    focused_workspace = ""

    for display in i3_displays:
        if display['active'] == True:
            disp = { "name":display['name'], "workspaces":[] }
            layout.append(disp)

    for workspace in i3_workspaces:
        for output in layout:
            if workspace['output'] == output['name']:
                output['workspaces'].append(workspace['num'])

        if workspace['focused'] == True:
            focused = workspace['num']

    for output in layout:
        if focused in output['workspaces']:
            focused_workspace = output['name']
    
    return layout, focused, focused_workspace

def parseOptions(arguments=sys.argv):
    args = arguments[1:]
    if len(args) != 1:
        print("Usage: {} prev|next".format(arguments[0]))
        exit(1)

    return args[0]

def goPrev(layout, focused, focused_workspace):
    for workspace in layout:
        if workspace['name'] == focused_workspace:
            try:
                index = workspace['workspaces'].index(focused)
            except:
                print("Error: Could not find focused workspace on focused display")
                exit(0)
            
            if index == 0:
                index = len(workspace['workspaces'])

            subprocess.run(["i3-msg", "workspace", "number", str(workspace['workspaces'][index - 1])])

            break
            
def goNext(layout, focused, focused_workspace):
    for workspace in layout:
        if workspace['name'] == focused_workspace:
            try:
                index = workspace['workspaces'].index(focused)
            except:
                print("Error: Could not find focused workspace on focused display")
                exit(0)
            
            if index == len(workspace['workspaces']) - 1:
                index = -1

            subprocess.run(["i3-msg", "workspace", "number", str(workspace['workspaces'][index + 1])])

            break

def main():
    layout, focused, focused_workspace = getLayout()
    direction = parseOptions()

    if direction == "prev":
        goPrev(layout, focused, focused_workspace)
    if direction == "next":
        goNext(layout, focused, focused_workspace)


main()