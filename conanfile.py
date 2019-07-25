from conans import ConanFile, CMake

class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    author = "Jamie Westell jwestell@gmail.com"
    url = ""
    license = "license"
    description = "Hello, World!"
    settings = "os", "compiler", "build_type", "arch"
    scm = {
        "type": "git",
        "subfolder": "hello",
        "url": "https://github.com/jwestell/hello.git",
        "revision": "master"
    }
    revision_mode = "scm"

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
