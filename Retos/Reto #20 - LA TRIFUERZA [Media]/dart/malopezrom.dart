void triforceRecursive(int level, [int currentLevel = 0]) {
  if (currentLevel == level * 2) {
    return;
  }

  String row;
  int firstLevel = level * 2 - 1;
  int secondLevel = 0;

  if (currentLevel < level) {
    row = ' ' * (firstLevel - currentLevel);
    row += printPoint(currentLevel);
  } else {
    secondLevel = currentLevel - level;
    row = ' ' * ((level - secondLevel) - 1);
    row += printPoint(secondLevel);
    row += ' ' * (2 * (level - secondLevel) - 1);
    row += printPoint(secondLevel);
  }

  print(row);

  triforceRecursive(level, currentLevel + 1);
}

String printPoint(int level) {
  return '*' * (2 * level + 1);
}

void main() {
  triforceRecursive(5);
}
