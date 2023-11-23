import subprocess

# Disable any existing swap
subprocess.run(["sudo", "swapoff", "-a"])

# Create a swap file with the specified size (8 GB in this example)
subprocess.run(["sudo", "dd", "if=/dev/zero", "of=/swapfile", "bs=1M", "count=8192"])

# Make the swap file usable as swap
subprocess.run(["sudo", "mkswap", "/swapfile"])

# Enable the new swap file
subprocess.run(["sudo", "swapon", "/swapfile"])

# Set the correct permissions on the swap file
subprocess.run(["sudo", "chmod", "600", "/swapfile"])

# Display the swap information
subprocess.run(["sudo", "swapon", "--show"])



# # for shell script 

# #!/bin/bash

# # Disable any existing swap
# sudo swapoff -a

# # Create a swap file with the specified size (8 GB in this example)
# sudo dd if=/dev/zero of=/swapfile bs=1M count=8192

# # Make the swap file usable as swap
# sudo mkswap /swapfile

# # Enable the new swap file
# sudo swapon /swapfile

# # Set the correct permissions on the swap file
# sudo chmod 600 /swapfile

# # Display the swap information
# sudo swapon --show


# # Save the file with a .sh extension, for example, create_swap.sh.

# # Make the script executable by running the following command:

# chmod +x create_swap.sh

# # To execute the script, run:
# ./create_swap.sh

# # This script will automatically execute all the commands you listed
# # in your question, and it will create and enable a swap file without 
# # needing to run each command one by one manually.