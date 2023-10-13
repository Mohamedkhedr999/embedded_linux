cmake_minimum_required(VERSION 3.15)
project(Pc_control CXX)


add_executable(Pc_control pc_control.cpp Server_Handler.cpp execute_command.cpp)
