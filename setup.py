from setuptools import setup, find_packages

setup(
    name="sapiens-inference",
    version="0.2.0",
    description="Run Sapiens Human Foundation models in Pytorch",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ibai Gorordo",
    license="MIT",
    packages=find_packages(include=["sapiens_inference", "sapiens_inference.*"]),
    install_requires=[
        "torch",
        "opencv-python",
        "torchvision",
        "huggingface_hub",
        "ultralytics",
        "cap_from_youtube",
        "imread_from_url",
    ],
    extras_require={
        "export": [
            "onnx",
            "onnxruntime",
        ],
    },
    url="https://github.com/ibaiGorordo/Sapiens-Pytorch-Inference",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)