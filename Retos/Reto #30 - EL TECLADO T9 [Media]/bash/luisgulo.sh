#!/bin/bash
<<PROGRAM_INFO
  Author: Luis G.L. (luisgulo)
  Program-Name: TecladoT9
  Program-Alias for 'Reto mouredev': luisgulo.sh
  Version: 0.2
  Changelog
    0.1: All keys (big array)
    0.2: Simple key array
  Notes: Exit program with: [Enter] + [-]
   
  Check program in Bash:
  echo "6-666-88-777-33-3-33-888" | ./luisgulo.sh
  or
  ./luisgulo.sh (and key press)
PROGRAM_INFO

# Array keys for T9 Keyboard
key[1]=',.?!'
key[2]='ABC'
key[3]='DEF'
key[4]='GHI'
key[5]='JKL'
key[6]='MNO'
key[7]='PQRS'
key[8]='TUV'
key[9]='WXYZ'
key[0]=' '
# Cursor position on the phone screen
TFIL=3; TCOL=6
TFR=16; TFC=13
Message=""
# Colours
REVERT='\e[7m'
NORMAL='\e[0m'

function PhoneKeyboard() {
   # Show a simulated phone with T9 keyboard
   tput cup 2 0
   echo '     ╔══════════════╗'
   echo -e "     ║$REVERT              $NORMAL║"
   echo '     ╠════╦════╦════╣'
   echo "     ║   1║   2║   3║"
   echo '     ║,.?!║ ABC║ DEF║'
   echo '     ╠════╬════╬════╣'
   echo '     ║   4║   5║   6║'
   echo '     ║ GHI║ JKL║ MNO║'
   echo '     ╠════╬════╬════╣'
   echo '     ║   7║   8║   9║'
   echo '     ║PQRS║ TUV║WXYZ║' 
   echo '     ╠════╬════╬════╣'
   echo '     ║   -║   0║    ║'
   echo '     ║NEXT║   █║    ║'
   echo '     ╚════╩════╩════╝'
}

function ScreenOverFlow() {
  # Check screen overflow and clean it
  if [ $TCOL -eq 20 ]
  then
    tput cup 3 0
    echo -e "     ║$REVERT              $NORMAL║"
    TCOL=6
  fi
}

function TransformKeys() {
  # Transform keystroke into letters
  if [ "$pressed" == "" ]
  then
    PhoneKeyboard
    tput cup 17 5
    echo -e "Message: «$Message»\n"
    exit 0
  fi
  ScreenOverFlow
  tput cup  $TFIL $TCOL 
  if [ "$pressed" == "0" ]
  then
      Character='█'
      echo -en "$REVERT$Character$NORMAL"
  fi
  if [ "$key[$pressed]" != "" ]
  then
    IsNumber='^[0-9]+$' 
    if  [[ $pressed =~ $IsNumber ]] ; then
      KeyPressed=$(echo $pressed|cut -c 1)
      KeyPosition=${#pressed}
      Character=$(echo ${key[$KeyPressed]} | cut -c $KeyPosition)
      echo -en "$REVERT$Character$NORMAL"
    else
      # $Character=''
      TCOL=$(( TCOL -1 ))
    fi
  fi
  Message=$Message"$Character"
  TCOL=$(( TCOL + 1 )) 
}

# MAIN
tput clear
PhoneKeyboard
# Loop until 'ENTER-' is pressed
while true
do
  tput cup $TFR $TCR
  read -s -d '-' pressed
  TransformKeys
done


