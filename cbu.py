import sqlite3

def test_bankname_map():
    """ Using a Python class as scalar function. """
    
    class BankNameMap:
        """ A class mapping CBU number into Bank Name. """
        
        cmap = {
            '007':	'Banco de Galicia 14​ y Buenos Aires S.A.',
            '011':	'Banco de la Nación Argentina',
            '014':	'Banco de la Provincia de Buenos Aires',
            '015':	'Industrial and Commercial Bank of China S.A.',
            '016':	'Citibank N.A.',
            '017':	'BBvA Banco Francés S.A.',
            '018':	'The Bank of Tokyo-Mitsubishi UFJ, LTD.',
            '020':	'Banco de la Provincia de Córdoba S.A.',
            '027':	'Banco Supervielle S.A.',
            '029':	'Banco de la Ciudad de Buenos Aires',
            '030':	'Central de la República Argentina',
            '034':	'Banco Patagonia S.A.',
            '044':	'Banco Hipotecario S.A.',
            '045':	'Banco de San Juan S.A.',
            '046':	'Banco do Brasil S.A.',
            '060':	'Banco de Tucumán S.A.',
            '065':	'Banco Municipal de Rosario',
            '072':	'Banco Santander Río S.A.',
            '083':	'Banco del Chubut S.A.',
            '086':	'Banco de Santa Cruz S.A.',
            '093':	'Banco de la Pampa Sociedad de Economía Mixta',
            '094':	'Banco de Corrientes S.A.',
            '097':	'Banco Provincia del Neuquén S.A.',
            '143':	'Brubank S.A.U.',
            '147':	'Banco Interfinanzas S.A.',
            '150':	'HSBC Bank Argentina S.A.',
            '158':	'Openbank',
            '165':	'JP Morgan Chase Bank NA (Sucursal Buenos Aires)',
            '191':	'Banco Credicoop Cooperativo Limitado',
            '198':	'Banco de Valores S.A.',
            '247':	'Banco Roela S.A.',
            '254':	'Banco Mariva S.A',
            '259':	'Banco Itaú Argentina S.A.',
            '262':	'Bank of America National Association',
            '266':	'BNP Paribas',
            '268':	'Banco Provincia de Tierra del Fuego',
            '269':	'Banco de la República Oriental del Uruguay',
            '277':	'Banco Sáenz S.A.',
            '281':	'Banco Meridian S.A.',
            '285':	'Banco Macro S.A.',
            '295':	'American Express Bank LTD. S.A.',
            '299':	'Banco Comafi S.A.',
            '300':	'Banco de Inversión y Comercio Exterior S.A.',
            '301':	'Banco Piano S.A.',
            '305':	'Banco Julio S.A.',
            '309':	'Nuevo Banco de la Rioja S.A.',
            '310':	'Banco del Sol S.A.',
            '311':	'Nuevo Banco del Chaco S.A.',
            '312':	'MBA Lazard Banco de Inversiones S.A.',
            '315':	'Banco de Formosa S.A.',
            '319':	'Banco CMF S.A.',
            '321':	'Banco de Santiago del Estero S.A.',
            '322':	'Banco Industrial S.A.',
            '325':	'Deutsche Bank S.A.',
            '330':	'Nuevo Banco de Santa Fe S.A.',
            '331':	'Banco Cetelem Argentina S.A.',
            '332':	'Banco de Servicios Financieros S.A.',
            '336':	'Banco Bradesco Argentina S.A.',
            '338':	'Banco de Servicios y Transacciones S.A.',
            '339':	'RCI Banque S.A.',
            '340':	'BACS Banco de Crédito y Securitización S.A.',
            '341':	'Más Ventas S.A.',
            '384':	'Wilobank S.A.',
            '386':	'Nuevo Banco de Entre Ríos S.A.',
            '389':	'Banco Columbia S.A.',
            '405':	'Ford Credit Compañía Financiera S.A.',
            '406':	'Metrópolis Compañía Financiera S.A.',
            '408':	'Compañía Financiera Argentina S.A.',
            '413':	'Montemar Compañía Financiera S.A.',
            '415':	'Transatlántica Compañía Financiera S.A.',
            '428':	'Caja de Crédito Coop. La Capital del Plata LTDA.',
            '431':	'Banco Coinag S.A.',
            '432':	'Banco de Comercio S.A.',
            '434':	'Caja de Crédito Cuenca Coop. LTDA.',
            '437':	'Volkswagen Credit Compañía Financiera S.A.',
            '438':	'Cordial Compañía Financiera S.A.',
            '440':	'Fiat Crédito Compañía Financiera S.A.',
            '441':	'GPAT Compañía Financiera S.A.',
            '442':	'Mercedes-Benz Compañía Financiera Argentina S.A.',
            '443':	'Rombo Compañía Financiera S.A.',
            '444':	'John Deere Credit Compañía Financiera S.A.',
            '445':	'PSA Finance Argentina Compañía Financiera S.A.',
            '446':	'Toyota Compañía Financiera de Argentina S.A.',
            '448':	'Finandino Compañía Financiera S.A.',
            '453':	'Naranja X',
            '992':	'Provincanje S.A.'
            }    

        def __call__(self, name):
            try:
                bankcode = name[0:3]
                return self.cmap[bankcode]
            except KeyError:
                return None

    class CBUCodeValidator:
        """ A class to validate CBU number. """

        ponder1 = (7,1,3,9,7,1,3)
        ponder2 = (3,9,7,1,3,9,7,1,3,9,7,1,3)

        def __call__(self, name):
            try:
                bloq1ok = False
                bloq2ok = False
                sum1 = 0
                for i, e in enumerate(name):
                    if i == 7: break 
                    sum1 += int(e) * self.ponder1[i]
                lastdigitsum1 = str(sum1)[-1]
                if int(name[7]) != 0 and (10 - int(lastdigitsum1)) == int(name[7]):
                    bloq1ok = True
                if int(name[7]) == 0 and (10 - int(lastdigitsum1)) == 10:
                    bloq1ok = True
                sum2 = 0
                for i, e in enumerate(name):
                    if i < 8: continue
                    if i == 21: break
                    sum2 += int(e) * self.ponder2[i-8]
                lastdigitsum2 = str(sum2)[-1]
                if len(name) != 22:
                    return False
                if int(name[-1]) != 0 and (10 - int(lastdigitsum2)) == int(name[-1]):
                    bloq2ok = True
                if int(name[-1]) == 0 and (10 - int(lastdigitsum2)) == 10:
                    bloq2ok = True
                return bloq1ok and bloq2ok
                
            except KeyError:
                return None


    with sqlite3.connect(':memory:') as conn:
        conn.create_function('bankName', 1, BankNameMap())
        conn.create_function('validateCbu', 1, CBUCodeValidator())

        conn.execute('CREATE TABLE account_bank('\
            'cbu TEXT NOT NULL);')

        conn.executemany(
            'INSERT INTO account_bank VALUES(?);',
            ( ('2850590940090418135201',),
              ('0170231820000000010500',),
              ('0110590940090418135201',),
              ('0290590940090418135201',),
              ('9920590940090418135201',)
            ) )
            
        for bank_name, valid_code in conn.execute(
            'SELECT bankName(cbu), validateCbu(cbu) FROM account_bank;'):
            print(';'.join((bank_name, str(valid_code))))

test_bankname_map()