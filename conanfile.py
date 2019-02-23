from conans import ConanFile, CMake, tools

class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    author = "Jamie Westell jwestell@gmail.com"
    url = "https://github.com/jwestell/hello"
    license = "license"
    description = "Hello, World!"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone https://github.com/jwestell/hello.git")
        self.run("cd hello && git checkout master")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="hello")
        cmake.build()

    def package(self):
        self.copy("hello-world", dst="bin", keep_path=False)
        self.copy("*.h", dst="include", src="hello")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
