class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    HELD_VOLUME = 0

    def __init__(self) -> None:
        """
        Method to set default values for tv status, channel, and volume/mute.
        :param status: tv power status
        :param muted: tv mute status
        :param volume: tv volume
        :param channel: tv channel
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to alter tv power status
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to alter tv mute status
        :param muted: changes volume to min volume
        :param volume: is adjusted to min volume or pre-mute volume
        """
        if self.__status and not self.__muted:
            Television.HELD_VOLUME = self.__volume
            self.__volume = Television.MIN_VOLUME
            self.__muted = True
        elif self.__status:
            self.__volume = Television.HELD_VOLUME
            self.__muted = False

    def channel_up(self) -> None:
        """
        Method to increase tv channel or return to min channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease tv channel or return to max channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase tv volume/pre-mute volume if not max volume
        """
        if self.__status:
            if self.__muted:
                self.__volume = Television.HELD_VOLUME
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease tv volume/pre-mute volume if not min volume
        """
        if self.__status:
            if self.__muted:
                self.__volume = Television.HELD_VOLUME
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to report tv power status, channel, and volume.
        :return: tv status/channel/volume
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
