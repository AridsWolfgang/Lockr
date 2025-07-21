"""
###########################################################################################################################################################
# Project Title     :   Lockr
# Author            :   AridsWolfgangX
# Date              :   8th May, 2025
# Objective         :   To research, design, and build a cross-platform vault and password manager in Python, starting simple and evolving into a 
#                       secure, full-featured product with CLI, GUI, Web and Mobile interfaces.
# #########################################################################################################################################################
"""

# Importing Modules 
import os 
import sys 


# Banner Setup
def banner():
    print("===================================================================")
    print("[~]                  ^[*]^ Lockr Vaults ^[*]^                   [~]")
    print("[~]                     Privacy at it Peak                      [~]")
    print("[~]                          v.0.0.1                            [~]")
    print("===================================================================")


banner()

print("You are welcome aboard")
options = input("Are you new here if yes type (Register) else type (login): ")

if options == "Register or register":
    print("Kindly input the required information below: ")
elif options == "Login or login":
    print("Kindly input the required information below: ")
else:
    print("An input is required !!!!")

# Registration and Login Setup 
def register():
    print("")
