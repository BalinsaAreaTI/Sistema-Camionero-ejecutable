from datetime import datetime
import pyodbc
import os
class Conectar():
    def __init__(self):
    # ============================ Conexion para Access

        ruta_base_datos = os.path.join("Base_de_Datos", "bd_sistema_camioneras.accdb")
        # self.conexionsqlaccess = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Jhonf Huertas\Desktop\Sistema_Escritorio_Municipalidad-main\Base_de_Datos\bd_sistema_camioneras.accdb;')
        self.conexionsqlaccess = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + ruta_base_datos + ';'
        )
    # ============================
    def db_consulta_puertos_default(self):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            cursoracces.execute("SELECT * FROM tbl_puertos")
            resultados = cursoracces.fetchall()
            return resultados[0]
        except Exception as e:
            return None
    
    def db_consulta_usuarios(self):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            cursoracces.execute("SELECT * FROM tbl_users")
            resultados = cursoracces.fetchall()
            return resultados
        except Exception as e:
            return None
        
    def db_consulta_datosImpresora(self):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            cursoracces.execute("SELECT * FROM tbl_impresora")
            resultados = cursoracces.fetchall()
            return resultados[0]
        except Exception as e:
            return None
    
    def db_consulta_ultimoTicket(self):
        cursoracces = self.conexionsqlaccess.cursor()
        cursoracces.execute("SELECT TOP 1 idPesada FROM tbl_pesadas ORDER BY idPesada DESC")
        resultado = cursoracces.fetchone()
        return resultado[0] if resultado else 0
    
    def db_verificarUsuario(self, usuario, password):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            query = "SELECT * FROM tbl_users WHERE user = ? AND password = ?"
            cursoracces.execute(query, (usuario, password))
            resultado = cursoracces.fetchone()
            return resultado
        except Exception as e:
            return None
    
    def db_consulta_recorte_cadena(self):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            cursoracces.execute("SELECT * FROM tbl_cadena")
            resultados = cursoracces.fetchall()
            return resultados[0]
        except Exception as e:
            return None
    
    def db_buscaDatosGuardados(self, valor):
        try:
            cursor = self.conexionsqlaccess.cursor()
            sql = "SELECT proveedorGuardado,conductorGuardado,transportistaGuardado FROM tbl_datosGuardados WHERE placaGuardada = ?"
            cursor.execute(sql, (valor,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            return None
        
    def db_registrarPesadas(
        self, 
        nro_ticket, fecha_inicial, hora_inicial, fecha_final, hora_final, 
        peso_bruto, peso_tara, placa_vehicular, cliente, 
        conductor, producto, transportista, observacion
    ):
        """
        Registra los datos de pesadas en la base de datos.

        Args:
            nro_ticket (str): Número de ticket.
            fecha_inicial (str): Fecha de pesaje inicial.
            hora_inicial (str): Hora de pesaje inicial.
            fecha_final (str): Fecha de pesaje final.
            hora_final (str): Hora de pesaje final.
            peso_bruto (float): Peso bruto.
            peso_tara (float): Peso tara.
            placa_vehicular (str): Placa del vehículo.
            cliente (str): Cliente.
            conductor (str): Conductor.
            producto (str): Producto transportado.
            transportista (str): Transportista.
            observacion (str): Observación adicional.

        Returns:
            bool: True si se registra correctamente, False en caso contrario.
        """
        try:
            query = """
            INSERT INTO tbl_pesadas (
                idPesada, fechaPesajeInicial, fechaPesajeFinal, horaPesajeInicial, horaPesajeFinal, 
                pesoBruto, pesoTara, placaVehicular, cliente, 
                conductor, producto, transportista, observacion
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            # Uso de with para gestionar el cursor
            with self.conexionsqlaccess.cursor() as cursor:
                cursor.execute(
                    query, 
                    (
                        nro_ticket, fecha_inicial, fecha_final, hora_inicial, hora_final, 
                        peso_bruto, peso_tara, placa_vehicular, cliente, 
                        conductor, producto, transportista, observacion
                    )
                )
            # Confirmación de los cambios
            self.conexionsqlaccess.commit()
            return True

        except Exception as e:
            print(f"Error al registrar la pesada: {e}")
            return False

        
    def db_busca_tara_guardada(self, valor):
        try:
            cursor = self.conexionsqlaccess.cursor()
            sql = "SELECT taraGuardada FROM tbl_datosGuardados WHERE placaGuardada = ?"
            cursor.execute(sql, (valor,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            return None
        
    def db_actualizarPesadas(self, txtNroTicket,txtFechaInicial,txtHoraInicial,txtFechaFinal,txtHoraFinal,txtPesoBruto,txtPesoTara,txtPlacaVehicular,txtCliente,txtConductor,txtProducto,txtTransportista,txtObservacion):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            query = "UPDATE tbl_pesadas SET fechaPesajeInicial = ?, fechaPesajeFinal = ?, horaPesajeInicial = ?, horaPesajeFinal = ?, pesoBruto = ?, pesoTara = ?, placaVehicular = ?, cliente = ?, conductor = ?, producto = ?, transportista = ?, observacion = ? WHERE idPesada = ?" 
            cursoracces.execute(query, (txtFechaInicial,txtFechaFinal, txtHoraInicial,txtHoraFinal,txtPesoBruto,txtPesoTara,txtPlacaVehicular,txtCliente,txtConductor,txtProducto,txtTransportista,txtObservacion,txtNroTicket))
            self.conexionsqlaccess.commit()
            return True
        except Exception as e:
            return False
        
    def db_verificarPlacaExistente(self, txtPlacaVehicular):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            query = "SELECT * FROM tbl_datosGuardados WHERE placaGuardada = ?"
            cursoracces.execute(query, (txtPlacaVehicular,))
            resultado = cursoracces.fetchone()
            return resultado
        except Exception as e:
            return None
        
    def db_actualizarDatosGuardados(self, txtPlacaVehicular,txtCliente,txtConductor,txtTransportista):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            query = "UPDATE tbl_datosGuardados SET placaGuardada = ?, proveedorGuardado = ?, conductorGuardado = ?, transportistaGuardado = ? WHERE placaGuardada = ?" 
            cursoracces.execute(query, (txtPlacaVehicular,txtCliente,txtConductor,txtTransportista,txtPlacaVehicular))
            self.conexionsqlaccess.commit()
            return True
        except Exception as e:
            return False
        
    def db_actualizarDatosGuardadosTara(self, txtPesoTara):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            query = "UPDATE tbl_datosGuardados SET taraGuardada = ? WHERE placaGuardada = ?" 
            cursoracces.execute(query, (txtPesoTara,))
            self.conexionsqlaccess.commit()
            return True
        except Exception as e:
            return False
        
    def db_registrarDatosGuardados(self, txtPlacaVehicular,txtCliente,txtConductor,txtTransportista,txtPesoTara):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            query = "INSERT INTO tbl_datosGuardados (placaGuardada,proveedorGuardado,conductorGuardado,transportistaGuardado,taraGuardada) VALUES (?,?,?,?,?,?)"
            cursoracces.execute(query, (txtPlacaVehicular,txtCliente,txtConductor,txtTransportista,txtPesoTara))
            self.conexionsqlaccess.commit()
            return True
        except Exception as e:
            return False
        
    def db_listarPesosTabla(self, fecha):
        try:
            cursoracces = self.conexionsqlaccess.cursor()
            query = ("SELECT idPesada,placaVehicular,fechaPesajeInicial,horaPesajeInicial,pesoBruto,pesoTara FROM tbl_pesadas WHERE fechaPesajeInicial = ?")
            cursoracces.execute(query, (fecha,))
            resultados = cursoracces.fetchall()
            return resultados
        except Exception as e:
            return None
        
    def db_traerDatosAnteriores(self, id_pesada):
        """
        Recupera los datos de una pesada específica en la base de datos.

        Args:
            id_pesada (int): ID de la pesada a buscar.

        Returns:
            list: Lista de resultados obtenidos de la base de datos.
            None: Si ocurre un error durante la consulta.
        """
        try:
            query = "SELECT * FROM tbl_pesadas WHERE idPesada = ?"
            
            # Uso de with para manejar automáticamente el cierre del cursor
            with self.conexionsqlaccess.cursor() as cursor:
                cursor.execute(query, (id_pesada,))
                resultados = cursor.fetchall()
            
            return resultados

        except Exception as e:
            # Loguear el error para depuración
            print(f"Error al ejecutar la consulta SQL para idPesada {id_pesada}: {e}")
            return None

    
    # def consulta_pesos_default(self):
    #     cursoracces = self.conexionsqlaccess.cursor()
    #     cursoracces.execute("SELECT * FROM tbl_pesos")
    #     resultados = cursoracces.fetchall()
    #     return resultados[0]
    
    # def consulta_tiempos_default(self):
    #     cursoracces = self.conexionsqlaccess.cursor()
    #     cursoracces.execute("SELECT * FROM tbl_tiempos")
    #     resultados = cursoracces.fetchall()
    #     return resultados[0]
    
    # def guardar_pesos(self, primer_peso_text, segundo_peso_text, tercer_peso_text):
    #     cursoracces = self.conexionsqlaccess.cursor()
    #     query = "UPDATE tbl_pesos SET bd_primer_peso = ?, bd_segundo_peso = ?, bd_tercer_peso = ? WHERE Id_pesos = 1"
    #     cursoracces.execute(query, (primer_peso_text, segundo_peso_text, tercer_peso_text))
    #     self.conexionsqlaccess.commit()