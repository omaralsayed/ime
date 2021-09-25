#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

int main() {
  const int PATH_MAX = 1024;

  FILE* fp;

  int status;
  char path[PATH_MAX];

  std::string text = "text";
  std::string command = "python bertweet.py --sentiment " + text;

  fp = popen(command.c_str(), "r");
  if (!fp) {
    std::cout << "There was an error executing popen()!" << std::endl;
    return 1;
  }

  while (fgets(path, PATH_MAX, fp))
    std::cout << path << std::endl;

  status = pclose(fp);
  if (status == -1) {
    std::cout << "Invalid status code!" << std::endl;
    return 1;
  }

  std::string sentiment;
  std::ifstream in("sentiment.txt");
  if (in.is_open()) {
    while (getline(in, sentiment)) {
      std::cout << sentiment;
    }

    in.close();
  }

  return 0;
}