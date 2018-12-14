
#include <iostream>
#include "glm/glm.hpp"

#include "utils/utils.hpp"

int main(int argc, const char **argv)
{
	auto m = glm::mat4(1.f);
	std::cout << m[0][0] << std::endl;
}