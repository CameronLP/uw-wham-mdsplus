#!/bin/bash
################################################################################
## Written by: Ethan Peterson
## Contact Info: ethan.peterson@wisc.edu
## Date: 08/4/2016
##
## Main shell script for running data acquisition/processing sequence
##
## Creates new MDSplus raw trees and sets up digitizers in parallel, once the 
## digitizers write to the trees, processing scripts can be run. Logs output
## to file.
##
## Modified by: Jason Milhone
## Contact Info: jason.m.milhone@gmail.com
## Date: 10/01/2020
##
## Removed a lot of extra stuff that was originally in here for BRB
##
## Modified again: D. Endrizzi
## Contact: douglass.a.endrizzi@gmail.com
## Date: 2023/04/24
##
## Added features to include RedPitaya digitizers
##
################################################################################

main () {
    pushd /home/WHAMdata/WHAMmdsplus/bin/
    python create_next_pulse.py wham 
    popd
    SHOTNUM=$((16#$(hexdump -e '16 "%02x " "\n"' /data/wham_model/top/shotid.sys)))
    python populate_shot_master.py $SHOTNUM  
    ## Loop through all arguments and run appropriate digitizer functions
    for arg in $@;do
        choose_digitizer $arg
    done
    wait
}

choose_digitizer () {
    if [ -n "$1" ]; then
        IFS=',' read -ra INPUTARR <<< "$1"
        TARGET="${INPUTARR[0]}"
        case $TARGET in
            192.168.113.9*) run_trex_cell $1;;
            192.168.130.*) run_acq_196 $1;;                                 
##          192.168.131.*) run_redpitaya $1;;     ## ASK ALEX TO CREATE A NEW .131 or some network IP address specifically for digitizers
        esac
    else
        run_default 
    fi
}

run_trex_cell () {
    echo run_trex_cell is deprecated on wham
}

run_acq_196 () {
    IFS=',' read -ra INPUTARR <<< "$1"
    local TARGET="${INPUTARR[0]}"
    local ON="${INPUTARR[1]}"
    local CMDSUFFIX="direct_setup.sh"
    if [ "${INPUTARR[2]}" == 0 ]; then
        CMDSUFFIX="direct_fire.sh"
    fi
    local NUMSAMPLES="${INPUTARR[3]}"
    local SAMPLERATE="${INPUTARR[4]}"
    local CHANNELBLOCKMASK="${INPUTARR[5]}"
    local MODE="${INPUTARR[6]}"
    local MASTERCLOCK="${INPUTARR[7]}"
    local CLOCKDIV="${INPUTARR[8]}"
    local DELAY="${INPUTARR[9]}"
    case $TARGET in
        192.168.130.75 ) local CMD="./a370_"$CMDSUFFIX;;
        192.168.131.15 ) local CMD="./a374_"$CMDSUFFIX;;
    esac

    if [ "$ON" != 0 ]; then
        echo =======================================================================
        echo ACQ196 Board: ${CMD:2:4}
        echo IP Address: $TARGET
        echo Number of Samples: $NUMSAMPLES
        echo "Sample Rate (Hz): $SAMPLERATE"
        echo "Delay (s): $DELAY"
        echo Channel Block Mask: $CHANNELBLOCKMASK
        echo Operation Mode: $MODE
        echo "Master Clock Rate (Hz): $MASTERCLOCK"
        echo Master Clock Divisor: $CLOCKDIV
        echo SSH Command: "$CMD $NUMSAMPLES $SAMPLERATE $CHANNELBLOCKMASK $MODE $MASTERCLOCK $CLOCKDIV $DELAY $SHOTNUM"
        echo =======================================================================
        echo
        
        ssh root@$TARGET "$CMD $NUMSAMPLES $SAMPLERATE $CHANNELBLOCKMASK $MODE $MASTERCLOCK $CLOCKDIV $DELAY $SHOTNUM" &
    fi
}

run_redpitaya () {
    echo run_redpitaya currently not functioning


    ssh root@RP_$TARGET "$CMD $DEC $SHOTNUM"  
} 


run_default () {
    echo Need to complete this
}

main "$@"
