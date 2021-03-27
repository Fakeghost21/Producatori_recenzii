class ProducatorException(Exception):
    pass


class ProducatorValidator:
    def validate(self, producator):
        errori = []
        if producator.get_nume() == '':
            errori.append('Numele este gol')
        if errori:
            raise ProducatorException(errori)
