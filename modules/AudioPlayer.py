import os
import threading
import time

class AudioPlayer():
    def __init__(self) -> None:
        self._audioFilePath = None
        self._callback = None
        self._thread = None
        self._indexLib = 0
        self._timeSleepAfterPlayed = 0.01

        self._listLib = (
            (
                'simpleaudio',
                lambda: self._tryImport_simpleaudio(),
            ),
            (
                'pydub',
                lambda: self._tryImport_pydub(),
            ),
            (
                'playsound',
                lambda: self._tryImport_playsound(),
            ),
        )
      
    def tryImportLib(self) -> bool:
        if not self._audioFilePath:
            print('[ERROR] Bạn cần phải thêm đường dẫn audio trước khi gọi phương thức này')
            print('    Try: audioPlayer.setAudioFilePath("Đường dẫn đến file audio của bạn !") ')
            exit()

        if self._indexLib >= (len(self._listLib)-1):
            print('[ERROR] Đã thử import tất cả lib từ danh sách lib đang được hỗ trợ: ')
            for libName, _ in self._listLib:
                print(f'    - {libName} ')
            exit()

        for i in range(self._indexLib, len(self._listLib)):
            (libName, callback) = self._listLib[i]

            print(f'[i] Đang thử import thư viện {libName}')
            callbackResult = callback()

            if callbackResult:
                self._callback = callbackResult
                print(f'[=>] Import thành công thư viện {libName}')
                return True
        return False

    def play(self):
        if self._thread == None:
            self._thread = threading.Thread(target=lambda:self._tryPlayAudio())

        if self._thread.is_alive():
            return False
        else:
            self._thread = threading.Thread(target=lambda:self._tryPlayAudio())

        self._thread.start()
        return True

    def isPlaying(self):
        return self._thread.is_alive()

    def setAudioFilePath(self, filePath:str):
        if not os.path.exists(filePath):
            print(f'[ERROR] Không tồn tại file audio ở đường dẫn: "{filePath}" ')
            exit()
        
        self._audioFilePath = filePath
    
    def getIndexOfLib(self):
        return self._indexLib
    
    def setIndexOfLib(self, index:int):
        self._indexLib = index

    def getTimeSleepAfterPlayed(self)->float:
        return self._timeSleepAfterPlayed
    
    def setTimeSleepAfterPlayed(self, val:float)->bool:
        if val >= 0.01:
            self._timeSleepAfterPlayed = val
            return True
        
        print(f'[W] Không thể set timesleep nhỏ hơn 0.01 giây được ! val={val}')
        self._timeSleepAfterPlayed = 0.01
        return False
        

    # Danh sách phương thức dùng để import lib và trả ra callback để gọi play audio
    def _tryPlayAudio(self):
        try:
            self._callback()
            time.sleep(self._timeSleepAfterPlayed)
        except:
            print('\n[FIX] Đang thử sửa lỗi !!! \n')
            self._indexLib += 1
            if self.tryImportLib():
                self._tryPlayAudio()
    
    def _tryImport_simpleaudio(self):
        callbackFunc=None
        try:
            import simpleaudio
            objectPlayer = simpleaudio.WaveObject.from_wave_file(self._audioFilePath)
            callbackFunc = lambda: objectPlayer.play().wait_done()
        except:
            callbackFunc=None
        return callbackFunc
    
    def _tryImport_playsound(self):
        callbackFunc=None
        try:
            from playsound import playsound
            callbackFunc= lambda: playsound(self._audioFilePath)
        except:
            callbackFunc=None
        return callbackFunc

    def _tryImport_pydub(self):
        callbackFunc=None
        try:
            from pydub import AudioSegment
            from pydub.playback import play
            
            song = AudioSegment.from_wav(self._audioFilePath)
            callbackFunc= lambda: play(song)
        except:
            callbackFunc=None
        finally:
            return callbackFunc

        return None
