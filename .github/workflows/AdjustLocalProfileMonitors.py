# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Script to make adjustments to the Helios profile by adding in
# additional monitors by XML manipulation.  This should be more
# reliable than using diff-match-patch.
# There are still changes to be made after this script, but it is more
# efficient for these to be text substitutions.  These changes are not 
# committed.
# Arguments:
# 1. Filename for the original Helios Profile file
# 2. Filename for the monitor XML to be inserted into the profile 
# 3. Filename of the resultant Helios profile
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import sys
InputHeliosProfile = sys.argv[1]
hpfMonitorFileName1 = sys.argv[2]
OutputHeliosProfile = sys.argv[3]

print("Donor Helios Profile", InputHeliosProfile)
print("Monitor XML ", hpfMonitorFileName1)
print("New Helios Profile ", OutputHeliosProfile)

from defusedxml.ElementTree import parse
# parse the original input file
print("Reading existing profile: ",InputHeliosProfile)
et = parse(InputHeliosProfile)
root = et.getroot()
print("Reading additional monitor XML: ",hpfMonitorFileName1)
monitorsRoot = parse(hpfMonitorFileName1).getroot()

monitors = root.find('Monitors')
i = 0
li = []
for el in monitors.iter("Monitor"):
    i += 1
    if el.find("Children").text is None:
        print("schedule non-helios Monitor for removal", i, " location ", el.find("Location").text, " size ", el.find("Size").text)
        # monitors.remove(el)
        li.append(el)
    else:
        el.find("Location").text = "0,0"
        print("Processing Monitor", i, " location ", el.find("Location").text, " size ", el.find("Size").text)

print("Number of Removals: ", len(li))
for i in range(len(li)):
        monitors.remove(li[i])

print("Writing new profile: ",OutputHeliosProfile)
et.write(OutputHeliosProfile,encoding="UTF-8",xml_declaration=True)

