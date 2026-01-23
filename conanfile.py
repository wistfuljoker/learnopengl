from conan import ConanFile
from conan.tools.cmake import cmake_layout


class LearnOpenGL(ConanFile):
    generators = ("CMakeToolchain", "CMakeDeps")
    settings = ("os", "build_type", "arch", "compiler")

    def requirements(self):
        self.requires("glad/0.1.36")

    def build_requirements(self):
        self.tool_requires("cmake/[>=3.10]")

    def layout(self):
        cmake_layout(self)
