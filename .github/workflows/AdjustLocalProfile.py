# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Script to make adjustments to the Helios profile by adding in
# additional items by XML manipulation.  This should be more
# reliable than using diff-match-patch.
# There are still changes to be made after this script, but it is more
# efficient for these to be text substitutions.  These changes are not 
# committed.
# Arguments:
# 1. Filename for the original Helios Profile file
# 2. Filename for the Bindings XML to be inserted into the profile 
# 3. Filename of the resultant Helios profile
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import sys
InputHeliosProfile = sys.argv[1]
hpfBindingFileName1 = sys.argv[2]
OutputHeliosProfile = sys.argv[3]

print("Donor Helios Profile", InputHeliosProfile)
print("Binding XML ", hpfBindingFileName1)
print("New Helios Profile ", OutputHeliosProfile)

from defusedxml.ElementTree import parse
# parse the original input file
print("Reading existing profile: ",InputHeliosProfile)
et = parse(InputHeliosProfile)
root = et.getroot()
print("Reading additional binding XML: ",hpfBindingFileName1)
bindingsRoot = parse(hpfBindingFileName1).getroot()

# Insert the additional bindings at the start of the binding list 
for el in root:
    if el.tag == "Bindings":
        i = 0
        for mel in bindingsRoot:
            el.insert(i,mel)
            i += 1
            print("Adding Binding for ", mel.find("LuaScript").text)
        continue

print("Writing new profile: ",OutputHeliosProfile)
et.write(OutputHeliosProfile,encoding="UTF-8",xml_declaration=True)

