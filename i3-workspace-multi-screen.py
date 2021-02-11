#! /usr/bin/python
import subprocess, json, sys

def getLayout():

    try:
        i3_workspaces_raw = subprocess.check_output(['i3-msg', '-t', 'get_workspaces'])
    except subprocess.CalledProcessError as err:
        print(err)
    i3_workspaces = json.loads(i3_workspaces_raw)

    try:
        i3_outputs_raw = subprocess.check_output(['i3-msg', '-t', 'get_outputs'])
    except subprocess.CalledProcessError as err:
        print(err)
    i3_outputs = json.loads(i3_outputs_raw)

    outputs = []
    focused_output = ""
    focused_workspaces = []

    for workspace in i3_workspaces:

        if workspace['focused'] == True:
            focused_output = workspace['output']

    for output in i3_outputs:
        if output['active'] == False:
            continue

        outputs.append(output['name'])
        focused_workspaces.append(output['current_workspace'])

    return outputs, focused_output, focused_workspaces

def parseOptions(arguments=sys.argv):

    args = arguments[1:]
    if len(args) != 1:
        print("Usage: {} prev|next".format(arguments[0]))
        exit(1)

    return args[0]

def goPrevOutput(outputs, focused_output, focused_workspaces):

    try:
        index = outputs.index(focused_output)
    except:
        print("Error: Could not find focused workspace on focused display")
        exit(0)
    
    if index == 0:
        index = len(focused_workspaces)
    
    subprocess.run(["i3-msg", "workspace", "number", str(focused_workspaces[index - 1])])
    
            
def goNextOutput(outputs, focused_output, focused_workspaces):

    try:
        index = outputs.index(focused_output)
    except:
        print("Error: Could not find focused workspace on focused display")
        exit(0)
    
    if index == len(focused_workspaces) - 1:
        index = -1
    
    subprocess.run(["i3-msg", "workspace", "number", str(focused_workspaces[index + 1])])

def main():
    
    direction = parseOptions()

    if direction == "prev_num":
        subprocess.run(["i3-msg", "workspace", "prev"])
    if direction == "next_num":
        subprocess.run(["i3-msg", "workspace", "next"])

    if direction == "prev_same_output":
        subprocess.run(["i3-msg", "workspace", "prev_on_output"])
    if direction == "next_same_output":
        subprocess.run(["i3-msg", "workspace", "next_on_output"])

    if not "num" in direction and not "same" in direction:
        outputs, focused_output, focused_workspaces = getLayout()

    if direction == "prev_output":
        goPrevOutput(outputs, focused_output, focused_workspaces)
    if direction == "next_output":
        goNextOutput(outputs, focused_output, focused_workspaces)


main()