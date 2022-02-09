cmake_minimum_required(VERSION 3.2)

if(DEFINED ENV{TRAVIS_BUILD_NUMBER})
    set(COMMON_TBN $ENV{TRAVIS_BUILD_NUMBER})
else()
    set(COMMON_TBN 1)
    message(WARNING "TRAVIS_BUILD_NUMBER env variable is undefined! It is set to 1.")
endif()

project(mybenchmark VERSION 0.0.${COMMON_TBN})

#find_package(benchmark REQUIRED)
#set(DLIB dlib::dlib)
#include_directories(${dlib_INCLUDE_DIRS})



set(CMAKE_CXX_STANDARD 14)

add_executable(mybenchmark main.cpp)

target_include_directories(mybenchmark PRIVATE benchmark/include)

target_link_directories(mybenchmark PRIVATE benchmark/build/src)

target_link_libraries(mybenchmark benchmark)

if (MSVC)
    target_compile_options(mybenchmark PRIVATE
        /W4
    )
else ()
    target_compile_options(mybenchmark PRIVATE
        -Wall -Wextra -pedantic
    )
endif()