#f/bin/bash

participants=()

participant_exists() {
  local already_entered=false

  for entry in "${participants[@]}"; do
    if [[ "$entry" == "$1" ]]; then
      already_entered=true
      break
    fi
  done

  echo "$already_entered"
}

add_entry() {
  if [[ "$(participant_exists $1)" == false ]]; then
    participants+=("$1")
    echo "Successfully added $1 to the list!"
  else
    echo "The name $1 was already registered..."
  fi
} 

remove_entry() {
  if [[ "$(participant_exists $1)" == true ]]; then
    for i in "${!participants[@]}"; do
      if [[ ${participants[i]} = $1 ]]; then
        unset 'participants[i]'
      fi
    done

    for i in "${!participants[@]}"; do
      participants_copy+=("${participants[i]}")
    done

    participants=("${participants_copy[@]}")
    unset participants_copy
    echo "The name $1 was successfully removed!"
  else
    echo "There was no $1 to remove..."
  fi
}

list_entries() {
  for entry in "${participants[@]}"; do
    echo "$entry"
  done
}

pick_winner() {
  if [ ${#participants[@]} -eq 0 ]; then
    echo "The list of participants is empty."
  else
    winner="${participants[ $RANDOM % ${#participants[@]} ]}"

    echo "And the winner is: $winner! 🎉"
  fi
}

while true; do
  clear

  echo "What do you want to do?"
  echo "-----------------------"
  echo "1- List all participants."
  echo "2- Add a new participant."
  echo "3- Remove a participant."
  echo "4- Choose a lucky winner!"
  echo "5- EXIT"

  read -p "Choose an option: " user_option
  clear

  case $user_option in
    1)
      echo "Entry list"
      echo "----------"
      list_entries
      ;;

    2)
      read -p "Enter the name you wish to add: " new_name
      add_entry "$new_name"
      ;;

    3)
      read -p "Enter the name you wish to remove: " to_remove
      remove_entry "$to_remove"
      ;;

    4)
      pick_winner
      ;;

    5)
      exit 0
      ;;

    *)
      echo "Unknown option [$user_option]."
      ;;
  esac

  read -p $'\n'"Press <ENTER> to continue..."
done
