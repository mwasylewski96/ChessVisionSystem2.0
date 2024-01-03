from setuptools import setup, find_packages
setup(
    name='Chess-Vision-System-2.0',
    version='1.0.0',
    packages=find_packages(),
    package_data={
        'chessOds': ['chessCurrentGameTable.ods', 'chessInitGameTable.ods'],
        'chessTools': ['chessConfig.yaml'],
        'chessFletApp': [
            'chessGameFletApp/assets/background.png',
            'chessGameFletApp/assets/draw.png',
            'chessGameFletApp/assets/white_win.png',
            'chessGameFletApp/assets/black_win.png',
        ],
    },
    install_requires=[
        'customtkinter',
        'packaging',
        'ezodf',
        'lxml',
        'aiohttp',
        'python-socketio',
        'PyYAML',
        'opencv-python',
        'pywin32'
    ],
)
