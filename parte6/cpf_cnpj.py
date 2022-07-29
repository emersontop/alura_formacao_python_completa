from validate_docbr import CPF, CNPJ

class CpfCnpj:

    def __init__(self, documento, tipo_de_documento):
        self.tipo_de_documento = tipo_de_documento
        documento = str(documento)
        if self.tipo_de_documento == 'cpf':
            if self.cpf_e_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF Invalido!!!')
        elif self.tipo_de_documento == 'cnpj':
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else: 
                raise ValueError('CNPJ Ivalido!!!')

    def __str__(self):
        if self.tipo_de_documento == 'cpf':
            return self.format_cpf()
        elif self.tipo_de_documento == 'cnpj':
            return self.format_cnpj()


    def cpf_e_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('Quantidade de digitos inválida!!!')

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError('Quantidade de digitos inválida!!!')

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
