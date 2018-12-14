cmake_minimum_required(VERSION 3.2)

add_executable(ray main.cpp)

find_package(glm)
target_link_libraries(ray PUBLIC glm utils)
target_include_directories(ray PRIVATE ${CMAKE_SOURCE_DIR})