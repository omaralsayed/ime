#include <iostream>
#include <fstream>
#include <string>
#include <vector>

bool getFileContent(std::string fileName, std::vector<std::string>& vecOfStrs) {
    std::ifstream in (fileName.c_str());
    if (!in) {
        std::cerr << "Cannot Open: " << fileName << std::endl;
        return false;
    }

    std::string str;
    while (std::getline(in, str)) {
        if (str.size() > 0)
            vecOfStrs.push_back(str);
    }

    in.close();
    return true;
}

int main() {
    std::vector<std::string> fromVec;
    std::vector<std::string> toVec;
    std::vector<std::string> subjectVec;
    std::vector<std::string> bodyVec;

    bool from = getFileContent("entities/from.txt", fromVec);
    if (from) {
        for (std::string& line: fromVec)
            std::cout << line << std::endl;
    }

    bool to = getFileContent("entities/to.txt", toVec);
    if (to) {
        for (std::string& line: toVec)
            std::cout << line << std::endl;
    }

    bool subject = getFileContent("entities/subject.txt", subjectVec);
    if (subject) {
        for (std::string& line: subjectVec)
            std::cout << line << std::endl;
    }

    bool body = getFileContent("entities/body.txt", bodyVec);
    if (body) {
        for (std::string& line: bodyVec)
            std::cout << line << std::endl;
    }

    return 0;
}