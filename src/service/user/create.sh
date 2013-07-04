#!/bin/bash
#Your Command Below!!!
list=(
bind_sns.py
get_profile.py
login.py
logout.py
register.py
update_device.py
update_profile.py
)

cls=(
 BindSNS
 GetProfile
 Login
 Logout
 Register
 UpdateDevice
 UpdateProfile
)


declare -i i=0

for j in ${list[@]}
    sed 's/Template/${cls[$i]}/' template.py
     (( i=$i+1 ))
done

