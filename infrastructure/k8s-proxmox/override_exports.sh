#!/bin/bash

# load global exports
. ../../exports.sh

# perform overrides and additional exports
export TF_VAR_network_prefix_0="192.168.20"
export TF_VAR_network_prefix_1="192.168.21"
export TF_VAR_nameserver="192.168.1.1"
