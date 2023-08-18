#!/bin/bash


# Number of devices to create
num_devices=40

# Tree name
tree="ECH_RAW"


file="./populate_tree_rp_devices.sh.tmp"

touch $file

# Overwrite file
echo "" > $file

# Open tree for editting
echo "edit ${tree}" >> $file
echo "dir" >> $file



# Remove any existing device nodes
for ((i = 0; i < num_devices; i++)); do

	j=$((i + 1))
	str1="delete node "
	str2="RP_"
	str3=$(printf "%02d" "$j")
	str4=" /confirm"
    echo "${str1}${str2}${str3}${str4}" >> $file
done

# Add the new device nodes
for ((i = 0; i < num_devices; i++)); do

	j=$((i + 1))
	str1="add node "
	str2="RP_"
	str3=$(printf "%02d" "$j")
	str4=" /model=WHAM_RED_PITAYA"
    echo "${str1}${str2}${str3}${str4}" >> $file
done

echo "dir" >> $file

# Save and close the tree
echo "write" >> $file
echo "close" >> $file

mdstcl <<EOF
$(<${file})
EOF

rm ${file}

#mdstcl <<EOF
#delete node RP_01 /confirm
#EOF
