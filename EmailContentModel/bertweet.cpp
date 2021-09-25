#include <iostream>
#include "Python.h"

int main() {
  Py_Initialize();

  FILE * berTweetFile = fopen("bertweet.py", "r");
  if (berTweetFile) {
    PyRun_SimpleFile(berTweetFile, "bertweet.py");
    fclose(berTweetFile);
  }

  Py_Finalize();

  return 0;
}