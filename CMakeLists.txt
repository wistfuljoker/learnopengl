cmake_minimum_required(VERSION 3.10.0)
project(app VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable(app src/main.cpp src/glad.c)

target_include_directories(app PRIVATE ${CMAKE_SOURCE_DIR}/include)

find_package(OpenGL REQUIRED)
find_package(glfw3 CONFIG REQUIRED)

target_link_libraries(app PRIVATE
    OpenGL::GL
    glfw
)