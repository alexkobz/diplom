from abc import abstractmethod


class AnalyzeInterface:

    @abstractmethod
    def analyze(self, basefolder):
        pass
