from abc import abstractmethod


class CountInterface:

    @abstractmethod
    def count(self, basefolder):
        pass

    @abstractmethod
    def write_csv_file(self, basefolder, filename, counter):
        pass
