cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(hello)
add_executable(test-hello test.cpp)
target_link_libraries(test-hello hello::hello)

# CTest is a testing tool that can be used to test your project.
enable_testing()
add_test(NAME test-hello
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND test-hello)
