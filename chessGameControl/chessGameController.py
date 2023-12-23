from chessCalibrations.chessCalibration import ChessCalibrator
from chessCameraProcessing.chessCameraRecording import ChessCameraRecorder
from chessGameWriting.chessGameWriter import ChessGameWriter
from chessImageProcessing.chessColorDetection import ChessColorDetector
from chessImageProcessing.chessCornerDetector import ChessCornerDetector
from chessImageProcessing.chessSquareIdentifier import ChessboardIdentifier
from chessOds.chessOdsDataReaderWriter import ChessOdsDataReaderWriter


class ChessGameController:

    def __init__(
            self
    ):
        self.chess_camera = ChessCameraRecorder()
        self.chess_game_writer = ChessGameWriter(
            game_name="game"
        )
        self.chess_color_detector = ChessColorDetector()
        self.chess_corner_detector = ChessCornerDetector()
        self.chess_ods_data_r_w = ChessOdsDataReaderWriter()