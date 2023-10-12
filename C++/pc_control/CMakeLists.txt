cmake_minimum_required(VERSION 3.16)

PROJECT(pc_controller
        DESCRIPTION "a C++ app to control pc"
        LANGUAGES CXX)

add_executable(${PROJECT_NAME}
                ${CMAKE_SOURCE_DIR}/pc_control.cpp
                ${CMAKE_SOURCE_DIR}/src/execute_command.cpp
                ${CMAKE_SOURCE_DIR}/src/Server_Handler.cpp
                )

target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_SOURCE_DIR}/include)