#include <iostream>
#include <stdio.h>

int main() {
  const int PATH_MAX = 1024;

  FILE* fp;

  int status;
  char path[PATH_MAX];

  fp = popen("python bertweet.py", "r");
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

  return 0;
}